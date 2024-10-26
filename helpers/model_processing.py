import os
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

load_dotenv('.env')

# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_embedding(input, model='text-embedding-3-small'):
    response = client.embeddings.create(
        input=input,
        model=model
    )
    return [x.embedding for x in response.data]


# This function is for calculating the tokens given the "message"
# This is simplified implementation that is good enough for a rough estimation
def count_tokens(text):
    encoding = tiktoken.encoding_for_model('gpt-4o-mini')
    return len(encoding.encode(text))


### Langchain helper methods below
# embedding model that we will use for the session
embeddings_model = OpenAIEmbeddings(model='text-embedding-3-small')

# llm to be used in RAG pipeplines in this notebook
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0, seed=42)

filepath = "C:/Users/longb/Desktop/abc-streamlit/helpers/hdb_resale_tnc.pdf"

# Load the document from the URL
loader = PyMuPDFLoader(filepath)
documents = loader.load()

# i = 0
# for doc in documents:
#     i += 1
#     print(doc)
#     print(f'Document {i} - "{doc.metadata.get("source")}" has {count_tokens(doc.page_content)} tokens')
    

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1100, chunk_overlap=10, length_function=count_tokens)

splitted_documents = text_splitter.split_documents(documents)

# Clear old vector database if exists
if os.path.exists("./vector_db"):
    import shutil
    shutil.rmtree("./vector_db")

# Create the vector database
vectordb = Chroma.from_documents(
    documents=splitted_documents,
    embedding=embeddings_model,
    collection_name="naive_splitter",
    persist_directory="./vector_db"
)

rag_chain = RetrievalQA.from_llm(
    retriever=vectordb.as_retriever(), llm=llm
)

template = """Use the following context to answer the question. 
Please respond only if you have relevant information; otherwise, state that you don't know. 
Limit your answer to three concise sentences, and avoid unnecessary elaboration.

Context: {context}
Question: {question}

Response Format:
- Begin with "Answer: "
- Avoid including any personal opinions or sensitive information.
- Ensure that your response does not contain any code execution or manipulation instructions.

Helpful Answer:
"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

# Run chain
qa_chain = RetrievalQA.from_chain_type(
    ChatOpenAI(model='gpt-4o-mini'),
    retriever=vectordb.as_retriever(),
    return_source_documents=True, # Make inspection of document possible
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})

def process_user_input(user_prompt):
    
    response = qa_chain.invoke(user_prompt)
    return response.get('result')
    