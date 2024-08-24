from dotenv import load_dotenv
import os
from langchain_community.vectorstores import FAISS
from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
import time
import streamlit as st

#load environment variables
load_dotenv()

OPENAI_API_TYPE = os.getenv("OPENAI_API_TYPE")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
OPENAI_DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
OPENAI_DEPLOYMENT_VERSION = os.getenv("OPENAI_DEPLOYMENT_VERSION")

OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME = os.getenv("OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME")
OPENAI_ADA_EMBEDDING_MODEL_NAME = os.getenv("OPENAI_ADA_EMBEDDING_MODEL_NAME")



llm = AzureChatOpenAI(deployment_name=OPENAI_DEPLOYMENT_NAME,
                      model_name=OPENAI_MODEL_NAME,
                      azure_endpoint=OPENAI_DEPLOYMENT_ENDPOINT,
                      openai_api_version=OPENAI_DEPLOYMENT_VERSION,
                      openai_api_key=OPENAI_API_KEY,
                      openai_api_type=OPENAI_API_TYPE)

embeddings=AzureOpenAIEmbeddings(deployment=OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME,
                            model=OPENAI_ADA_EMBEDDING_MODEL_NAME,
                            azure_endpoint=OPENAI_DEPLOYMENT_ENDPOINT,
                            openai_api_type=OPENAI_API_TYPE,
                            chunk_size=1)


# Initialize gpt-35-turbo and our embedding model
#load the faiss vector store we saved into memory
def load_vector_ini_model(indexPath, name):

    vectorStore = FAISS.load_local(f"{indexPath}{name}", embeddings, allow_dangerous_deserialization=True)

    retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k":2})


    template = """Answer the following question based on the provided context
    <context>
    {context}
    </context>

    Question:{input}
    """

    #This creates a chain that will combine documents and use the provided template and language model to generate responses.
    prompt = ChatPromptTemplate.from_template(template)
    document_chain = create_stuff_documents_chain(llm,prompt)

    # Example usage
    context = "The sun rises in the east and sets in the west."
    question = "Which direction does the moon set?"

    # Convert context into a Document object
    documents = [Document(page_content=context)]

    retrieval_chain = create_retrieval_chain(retriever,document_chain)

    return retrieval_chain


# Function to generate output based on a query
def make_output(retrieval_chain, query):
    response = retrieval_chain.invoke({"input": f"{query}"})
    result = response["answer"]

    return result

# Function to modify the output by adding spaces between each word with a delay
def modify_output(input):
    # Iterate over each word in the input string
    for text in input.split():
        # Yield the word with an added space
        yield text + " "
        # Introduce a small delay between each word
        time.sleep(0.05)