import streamlit as st 

# Set page configuration including title and icon
st.set_page_config(page_title="Summary",
                   page_icon="📋", layout='wide')

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

summaries = {'Test': 'Testing Script'}
    
# Display a markdown header for the report summary
st.markdown("# 📋 Report Summary")

# Iterate over each title and corresponding text in the summaries
for title, text in summaries.items():
    # Display each title as a markdown sub-header
    st.markdown(f"### {title}")
    # Display the text associated with the title
    st.markdown(text)

# from dotenv import load_dotenv
# import os
# import openai
# from langchain_community.vectorstores import FAISS
# from langchain_openai import AzureChatOpenAI
# from langchain_openai import AzureOpenAIEmbeddings
# from langchain.prompts import PromptTemplate
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.documents import Document
# from app_indexer import embed_file
# import references

# #load environment variables
# load_dotenv()

# OPENAI_API_TYPE = os.getenv("OPENAI_API_TYPE")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
# OPENAI_DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")
# OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
# OPENAI_DEPLOYMENT_VERSION = os.getenv("OPENAI_DEPLOYMENT_VERSION")

# OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME = os.getenv("OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME")
# OPENAI_ADA_EMBEDDING_MODEL_NAME = os.getenv("OPENAI_ADA_EMBEDDING_MODEL_NAME")

# #init Azure OpenAI
# openai.api_type = OPENAI_API_TYPE
# openai.api_version = OPENAI_DEPLOYMENT_VERSION
# openai.azure_endpoint = OPENAI_DEPLOYMENT_ENDPOINT
# openai.api_key = OPENAI_API_KEY


# from langchain_core.documents import Document

# llm = AzureChatOpenAI(deployment_name=OPENAI_DEPLOYMENT_NAME,
#                       model_name=OPENAI_MODEL_NAME,
#                       azure_endpoint=OPENAI_DEPLOYMENT_ENDPOINT,
#                       openai_api_version=OPENAI_DEPLOYMENT_VERSION,
#                       openai_api_key=OPENAI_API_KEY,
#                       openai_api_type=OPENAI_API_TYPE)

# embeddings=AzureOpenAIEmbeddings(deployment=OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME,
#                             model=OPENAI_ADA_EMBEDDING_MODEL_NAME,
#                             azure_endpoint=OPENAI_DEPLOYMENT_ENDPOINT,
#                             openai_api_type=OPENAI_API_TYPE,
#                             chunk_size=1)

# vectorStore = FAISS.load_local("./dbs/documentation/Test", embeddings, allow_dangerous_deserialization=True)

# retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k":2})

# # Define prompt
# prompt = ChatPromptTemplate.from_messages(
#     [("system", """Extract the person name, company name, location and phone number from the text below:\n {context}""")]
# )

# # Instantiate chain
# chain = create_stuff_documents_chain(llm, prompt)

# retrieval_chain = create_retrieval_chain(retriever,chain)

# # Invoke chain
# result = retrieval_chain.invoke({"input": """Extract the person name, company name, location and phone number from the text below:\n document"""})

# print(result['answer'])
