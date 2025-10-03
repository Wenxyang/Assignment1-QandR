import streamlit as st
import os
import shutil
from utilities.question_answer import question_answer

st.title("File Upload Example (Overwrite Mode)")

uploaded_file = st.file_uploader("Please upload a file", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    # Clear the "data" folder before saving
    shutil.rmtree("data", ignore_errors=True)  # delete the folder if it exists
    os.makedirs("data")                        # recreate empty folder

    # Save the new file
    save_path = os.path.join("data", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File successfully saved to {save_path}. (Old files removed)")

# Sidebar: API key input
with st.sidebar:
    st.header("🔑 OpenAI API Key")
    API_KEY = st.text_input("Enter your API Key", type="password")
    if API_KEY:
        os.environ["OPENAI_API_KEY"] = API_KEY
        st.success("API Key set successfully ✅")
    else:
        # remove key if previously set
        if "OPENAI_API_KEY" in os.environ:
            del os.environ["OPENAI_API_KEY"]
        st.warning("Please enter your API Key.")

question = st.text_input("Enter your question:")
if st.button("Ask"):
    if question.strip():
        if not os.environ.get("OPENAI_API_KEY"):
            st.error("You must enter your OpenAI API Key in the sidebar first.")
        else:
            answer = question_answer(question)
            st.write("**Answer:**")
            st.write(answer)
    else:
        st.warning("Please type a question first.")