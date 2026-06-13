from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

db_path = os.getenv("db_path") # make sure db folder contain vector database that created using jupyter
embedding_model_path = os.getenv("embedding_model_path")

class Retriever:
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=embedding_model_path,
            model_kwargs={"device":"cpu"},
            encode_kwargs={"normalize_embeddings":True}
        )

        self.db = Chroma(
            persist_directory=db_path,
            embedding_function=self.embedding_model
        )

    def get_relevant_docs(self, updated_question):
        
        # define retriever
        retriever = self.db.as_retriever(search_kwargs={"k":3})

        # get relevant docs as a list
        docs = retriever.invoke(updated_question)

        
        return docs # list of Documents
