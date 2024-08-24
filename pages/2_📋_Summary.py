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
