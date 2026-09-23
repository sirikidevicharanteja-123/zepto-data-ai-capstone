# retrieval.py

from ingestion import collection, embedding_model


def retrieve_documents(query: str, top_k: int = 3):
    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]
    document_ids = results["ids"][0]

    return documents, document_ids