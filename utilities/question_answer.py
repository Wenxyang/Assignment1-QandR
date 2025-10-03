from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

def question_answer(question):
    # Load documents from the data folder
    documents = SimpleDirectoryReader("data").load_data()
    # Build index
    index = VectorStoreIndex.from_documents(documents)
    # Create query engine
    query_engine = index.as_query_engine()
    # Ask the question
    response = query_engine.query(question)
    return str(response)