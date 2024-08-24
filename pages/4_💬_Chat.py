import streamlit as st 
from utils import load_vector_ini_model,make_output, modify_output 
import references
from importlib import reload
from app_indexer import embed_file
import os

# try:
#     st.session_state = session
# except:
#     # Set page configuration including title and icon
st.set_page_config(page_title="ChatBot",
                page_icon="🤔", layout='wide')

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

# Display the title of the chat interface
st.title("💬 Chat with the Report")

reload(references)
file_names = references.input_files

drpdwn = st.selectbox(options=file_names, label=f'Select Report Name ({len(file_names)} files available):', index=None)

if drpdwn is None:
    st.header('Select a report to chat with it')
else:
    if drpdwn[:-4] not in os.listdir(references.outputPath):
        try:
            embed_file(drpdwn, references.dataPath, references.outputPath, drpdwn)
        except:
            st.write(f'Format not supported for {drpdwn}')

    if drpdwn[:-4] in os.listdir(references.outputPath):

        retrieval_chain = load_vector_ini_model(references.outputPath, drpdwn[:-4])

        # Initialize session state to store chat messages if not already present
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display previous chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Accept user input in the chat interface
        if prompt := st.chat_input(f"What is your question for {drpdwn[:-4]}?"):
            # Display user input as a chat message
            with st.chat_message("user"):
                st.markdown(prompt)
            # Append user input to session state
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Get response from the chatbot based on user input
            response = make_output(retrieval_chain, prompt)
            
            # Display response from the chatbot as a chat message
            with st.chat_message("assistant"):
                # Write response with modified output (if any)
                st.write_stream(modify_output(response))
            # Append chatbot response to session state
            st.session_state.messages.append({"role": "assistant", "content": response + f'(Response for:  {drpdwn[:-4]})'})

session = st.session_state






 