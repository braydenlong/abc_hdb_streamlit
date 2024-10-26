import streamlit as st


st.title('Methodology')

st.markdown("""
### Environment Setup

- Loading of environment variables from a .env file, containing the OpenAI API key.
- Initialising of the OpenAI client using the API key retrieved from the environment.

### Embedding Function

- Using the OpenAI API to get embeddings for the input text. It returns a list of embeddings for the provided input.

### Token Counting

- To count the number of tokens in a given text using the tiktoken library for 'gpt-4o-mini', to understand input sizes and costs associated with API calls.

### Document Loading

- Initialising a document loader using PyMuPDF to read the required data and loads the content of the PDF into a list of document objects.


### Text Splitting

- Initialising a text splitter that divides the documents into smaller chunks for better handling during processing. It uses a specified chunk size and overlap, leveraging the `count_tokens` function to measure length.

### Vector Database Creation

- Checks if a vector database directory exists and removes it if found. Creates a vector database using the split document chunks and their embeddings. It persists the database in a specified directory, allowing for efficient retrieval.

### RAG Setup

- Sets up the RAG pipeline where a retriever is used in conjunction with a language model (LLM) to answer queries based on retrieved documents.

### Prompt Template

- The `template` variable defines how the context and questions should be structured for the language model. It emphasizes conciseness, relevance, and avoidance of personal opinions.

### Final QA Chain

- Creation of the final QA chain, using the LLM and the retriever, with the ability to return source documents for inspection.

### Processing User Input

- To take in a user query, invokes the QA chain, and returns the answer. The function retrieves the result from the response object.

### Data Flow

1. **Input Handling**: The user provides a query.
2. **Document Loading**: The specified data is loaded and processed into a list of document objects.
3. **Text Splitting**: The loaded documents are split into manageable chunks to facilitate efficient retrieval.
4. **Embedding Generation**: The chunks are converted into embeddings and stored in a vector database.
5. **Retrieval**: When a query is made, the system retrieves relevant document chunks based on the embeddings.
6. **Response Generation**: The retrieved context is fed to the language model, which generates a concise answer based on the prompt template.
7. **Output**: The generated answer is returned to the user.
""")


image_path_1 = "C:/Users/longb/Downloads/abc diagram_drawio_1.png"
st.image(image_path_1, caption='Flowchart for Use Case 1: Procedure for Buying a Resale HDB Flat',use_column_width=True)

image_path_2 = "C:/Users/longb/Downloads/abc diagram_drawio_2.png"
st.image(image_path_1, caption='Flowchart for Use Case 2: Terms and Conditions for Buying a Resale HDB Flat',use_column_width=True)