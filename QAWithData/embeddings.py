from llama_index.core import VectorStoreIndex, ServiceContext, Settings, load_index_from_storage
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithData.data_ingestion import load_data
from QAWithData.model_api import load_model

import os
import sys
from exception import customexception
from logger import logging

from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def download_gemini_embedding(model,doc):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001", api_key=GEMINI_API_KEY)
        
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.node_parser = SentenceSplitter(chunk_size=800, chunk_overlap=20)
        
        logging.info("")
        index = VectorStoreIndex(doc, embed_model=gemini_embed_model)
        index.storage_context.persist()
        
        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e,sys)