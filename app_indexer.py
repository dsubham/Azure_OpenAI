from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import openai
import os

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

#init Azure OpenAI
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_DEPLOYMENT_VERSION
openai.azure_endpoint = OPENAI_DEPLOYMENT_ENDPOINT
openai.api_key = OPENAI_API_KEY



def embed_file(file_name, dataPath, outputPath, out_index):
    embeddings=AzureOpenAIEmbeddings(deployment=OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME,
                                model=OPENAI_ADA_EMBEDDING_MODEL_NAME,
                                azure_endpoint=OPENAI_DEPLOYMENT_ENDPOINT,
                                openai_api_type=OPENAI_API_TYPE,
                                chunk_size=1)
    
    fileName = dataPath + file_name



    #use langchain PDF loader
    loader = PyPDFLoader(fileName)

    #split the document into chunks
    pages = loader.load_and_split()

    # #Use Langchain to create the embeddings using text-embedding-ada-002
    db = FAISS.from_documents(documents=pages, embedding=embeddings)

    # #save the embeddings into FAISS vector store
    # db.save_local("./dbs/documentation/faiss_index_new")

    db.save_local(f"{outputPath}{out_index[:-4]}")