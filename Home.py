import streamlit as st
import os
import shutil

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

from utilities.question_answer import question_answer

question = st.text_input("Enter your question:")
if st.button("Ask"):
    if question.strip():
        answer = question_answer(question)
        st.write("**Answer:**")
        st.write(answer)
    else:
        st.warning("Please type a question first.")