# ingestion.py

from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

# Paths and model configuration

DOCS_DIR = Path(__file__).parent / "docs"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

CHROMA_DB_DIR = Path(__file__).parent / "chroma_db"

COLLECTION_NAME = "zepto_policies"

# Load embedding model
embedding_model = SentenceTransformer(EMBEDDING_MODEL)

# Create ChromaDB client
chroma_client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))

collection = chroma_client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"}
)
# Load documents from docs folder

def load_documents():
    documents = []
    
    for file_path in sorted(DOCS_DIR.glob("*.txt")):
        text = file_path.read_text(encoding="utf-8").strip()
        
        documents.append({
            "id": file_path.stem,
            "text": text
        })
    
    return documents

# Embed and store documents in ChromaDB

def ingest_documents():
    documents = load_documents()

    for document in documents:
        embedding = embedding_model.encode(document["text"]).tolist()

        collection.upsert(
            ids=[document["id"]],
            documents=[document["text"]],
            embeddings=[embedding]
        )

# Run ingestion

if __name__ == "__main__":
    ingest_documents()
    print("Documents ingested successfully.")