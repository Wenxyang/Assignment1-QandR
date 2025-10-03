import streamlit as st
import os
import shutil
from utilities.question_answer import question_answer
from utilities.validate_check import validate_api_key

st.title("Queries and Responses")

uploaded_file = st.file_uploader("Please upload a file", type=["pdf", "docx", "txt"])
question = None

if uploaded_file is not None:
    # Clear the "data" folder before saving
    shutil.rmtree("data", ignore_errors=True)  # delete the folder if it exists
    os.makedirs("data")                        # recreate empty folder

    # Save the new file
    save_path = os.path.join("data", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Uploaded successfully ✅")

# Sidebar: API key input
with st.sidebar:
    st.header("🔑 OpenAI API Key")
    API_KEY = st.text_input("Enter your API Key", type="password")
    if API_KEY.strip():
        st.success("API Key set successfully ✅")
    else:
        st.warning("Please enter your API Key.")

question = st.text_input("Ask a question about your uploaded file:")
if st.button("Ask"):
    if not API_KEY or not validate_api_key(API_KEY):
        st.error("You must enter a valid OpenAI API Key in the sidebar first.")
    elif not question.strip():  
        st.warning("Please type your question.")
    else:
        answer = question_answer(question.strip(), API_KEY.strip())
        st.write("**Answer:**")
        st.write(answer)