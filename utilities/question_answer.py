from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI as LIOpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

def question_answer(question: str, api_key: str):
    key = (api_key or "").strip()

    # Explicitly inject this call’s API key into LlamaIndex.
    Settings.llm = LIOpenAI(api_key=key, model="gpt-5", temperature=0)
    Settings.embed_model = OpenAIEmbedding(api_key=key, model="text-embedding-3-large")

    # Load documents from the data folder
    documents = SimpleDirectoryReader("data").load_data()
    # Build index
    index = VectorStoreIndex.from_documents(documents)
    # Create query engine
    query_engine = index.as_query_engine(similarity_top_k=4)
    # Ask the question
    response = query_engine.query(question)
    return str(response)