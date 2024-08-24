import streamlit as st 
import references
from importlib import reload

# Set page configuration including title and icon
st.set_page_config(page_title="Hello",
                   page_icon="🙏", layout='wide')
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

st.title('AI Crusaders')

# Displaying a markdown header with a welcoming message and description
st.markdown("""
            # 👋 Welcome to the AI Assitant for Sustainable Investment
            Explore the features to perform a peer comparison for companies across the pillars of the TCFD report.
            """)
uploaded_files = st.file_uploader(label='Upload pdf documents', accept_multiple_files=True)

error = 0

if uploaded_files:
    for uploaded_file in uploaded_files:
        if uploaded_file.name[-4:] == '.pdf':
            with open(f'./data/documentation/{uploaded_file.name}', 'wb') as f:
                f.write(uploaded_file.getbuffer())
        else:
            error = 1
if error == 1:
    st.markdown(':red[Invalid file type. Please upload pdf files only]')

reload(references)
file_uploaded = references.input_files

try:
    st.markdown(f'`{len(file_uploaded)} files were uploaded - {file_uploaded}.` You may proceed to the view the other protect features')
except:
    pass

st.markdown("""
            ### 🛠 The features of the product:
            - Go to the `Context` page to the data for different pillars from the TCFD report (prototype: Governance)
            - Go to `Summary` page to get the summary
            - Go to the `Peer Comparison` page to get a comparative analysis for all the uploaded documents
            - Go to `Chat` page to ask questions related to the report
            """)
