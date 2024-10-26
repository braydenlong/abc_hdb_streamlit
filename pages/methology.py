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


image_path_1 = "https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=abc%20diagram.drawio#R%3Cmxfile%3E%3Cdiagram%20id%3D%22C5RBs43oDa-KdzZeNtuy%22%20name%3D%22Page-1%22%3E5VnZdpswEP0aP6aHxcb2Y73EXdImqZM4fVRgAqqFRISwcb6%2BkhEGQo5rdzmm5AWYq0HLnbkalo49DtMZR1HwhXlAOpbhpR170rEs07FMeVLIJkO6ppUBPseediqAOX4GDRoaTbAHccVRMEYEjqqgyygFV1QwxDlbV90eGamOGiEfasDcRaSOLrAnggwdWP0C%2FwDYD%2FKRTWeYtYQod9YriQPksXUJsqcde8wZE9lVmI6BKPJyXhYfNwtysXRmn67jJ3Q7%2Bnzz9e4s6%2Bz8mFt2S%2BBAxW93%2Fdy9H5qT2ery5jkmi%2FO76yt3fdbVSxObnC%2FwJH3aZFwEzGcUkWmBjjhLqAeqV0Nahc8FY5EETQn%2BACE2OhdQIpiEAhES3SpXwTf3%2Bv6t8V0Z73q5OUnLjZONtg6kQdMVs4S7sMfP1tmIuA%2F7%2BtOZoogppZQmeQYsBDlJ6cCBIIFX1bxDOn39nV8RInmho3REMuhZrxBJ9Eg3kAqJzCOChcDUV6NSTx7HQUKXW%2BBFjIsIqnCsAyxgHqEtWWu5C1Sj9cio0KGU0rdHPkFxrCMSC86WO10p751Ijg%2FYCriAdC%2FFurWnFam3JDNX6LoQ%2BA4LSuLuGn8elFdl1HvDMurXZfQqR2ajZNSvyWgaPoCnAmIZM6DA5SQYbZ10LKNp2um%2FDe3s08QvteOcSjv7Zl3Szp18cmNcFSF5Ug9kbZON7TRNNqZZI%2Fnt6MY5tOYYjRKOUxPON9kvBgm0TjE9q2mKGZ5CMH858Qf%2FZcEY1PL%2BNgZVLq4T0N23OfV7p8580z5JrUixuC9dlyqFtIpCoYx%2F9XxlHFoorEYJJp93pVLEEaMxtPv1xBk2rWrkmVEKxWUiokS0jvtB4z6rmL0a9y2o4Wa3vint%2B9TXlD2pWwvGhLlJqEixjIuO5RChUjVCtBIh5ylRX8hHD8hd%2BttYnLmMyLdF%2B70akmKB5eOvYjn3lFe%2BOjPkZZ8z2aM8jJJNZl1x5oKXcIilMUEC5UPLZWWjZ7e3TqDyne%2BFQo0DFTo4XqHSLH5tbNtKP4js6U8%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E"
st.image(image_path_1, caption='Flowchart for Use Case 1: Procedure for Buying a Resale HDB Flat',use_column_width=True)

image_path_2 = "https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=abc%20diagram.drawio#R%3Cmxfile%3E%3Cdiagram%20id%3D%22C5RBs43oDa-KdzZeNtuy%22%20name%3D%22Page-1%22%3E5VnZdpswEP0aHtPDYmP7sV7iLumS2onTRwUmoFpIRAgv%2BfpKRhgIOa7d5ZiSF8NcDVruzNWAbDijaDPlKA4%2FMR%2BIYZv%2BxnDGhm1brm3Ji0K2GdKx7AwIOPa1UwHM8BNo0NRoin1IKo6CMSJwXAU9Ril4ooIhztm66vbASHXUGAVQA2YeInV0gX0RZmjf7hX4O8BBmI9suYOsJUK5s15JEiKfrUuQMzGcEWdMZHfRZgREkZfzsni%2FXZCrpTv9cJ08opvhx%2Fnn24uss8tTHtkvgQMVv931U%2BduYI2nqy%2Fzp4QsLm%2Bvv3rri45emtjmfIEv6dMm4yJkAaOITAp0yFlKfVC9mtIqfK4YiyVoSfAHCLHVuYBSwSQUiojoVrkKvr3Tz%2B%2BM78p4083N8abcON5q60gaNF0JS7kHB%2FwcnY2IB3CoP50piphSSmmSp8AikJOUDhwIEnhVzTuk0zfY%2BxUhkjc6Sickg571CpFUjzSHjZDILCZYCEwDNSr15e8oTOlyBzyLcRFBFY51iAXMYrQjay13gWq0HhgVOpRS%2Bs4wIChJdEQSwdlyryvlvRfJ6QFbARewOUixbu1qReotycoVui4EvsfCkrg75p8H5UUZdV%2BxjHp1Gb3IkdUoGfVqMppE9%2BCrgNjmFChwOQlGWycd22yadnqvQzuHNPFL7bjn0s6hWZe0cyvf3BhXRUhe1AtZ22TjuE2TjWXVSH49unGPrTlmo4Tj1oTzTfaLQQKtU0zXbppiBucQzF9O%2FP5%2FWTD6tby%2FSUCVi%2BsUdPdtTv3uuTPfcs5SKzZY3JXuS5VCWkWhUMa%2Fer8yjy0UdqMEk8%2B7UimSmNEE2v154g6aVjXyzCiF4ksq4lS0jvt%2B445VrG6N%2BxbUcKtT35QOHfU1ZU%2Fq1IIxZl4aKVJs88qwXSJUqsaIViLkPqbqhHx4j7xlsIvFhceI%2FFp03qohKRZYvv4qlnNPeReoK0N%2BdpzJHuTPHHiUGPuzTUZ9rLZABY2RQPn4cm3ZFLI%2BWqdS%2BeH3TKbmkTLtny5TaRb%2Fb%2BzaSv8SOZOf%3C%2Fdiagram%3E%3C%2Fmxfile%3E"
st.image(image_path_1, caption='Flowchart for Use Case 2: Terms and Conditions for Buying a Resale HDB Flat',use_column_width=True)