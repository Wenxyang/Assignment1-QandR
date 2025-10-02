from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

def question_answer(question):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    return str(response)