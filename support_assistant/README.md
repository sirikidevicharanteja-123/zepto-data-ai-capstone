# Zepto Support Assistant

The Support Assistant is a policy-based Retrieval-Augmented Generation (RAG) service for answering Zepto customer-support questions.

It uses:

- FastAPI for the API
- LangGraph for workflow orchestration
- Sentence Transformers for embeddings
- ChromaDB for vector retrieval
- A mock LLM mode for deterministic local execution
- Zepto policy documents as the knowledge base

---

## 1. Architecture

The overall workflow is:

    User Query
        ↓
    FastAPI /ask
        ↓
    LangGraph
        ↓
    Intent Classification
        ↓
    Policy Question?
       /       \
     Yes       No
      ↓         ↓
    Retrieve   Direct
    Documents  Answer
      ↓
    Sentence Transformer
      ↓
    ChromaDB
      ↓
    Top 3 Relevant Documents
      ↓
    Mock Answer Generation
      ↓
    Answer + Sources + Confidence

---

## 2. Project Structure

    support_assistant/
    │
    ├── docs/
    │   ├── doc_01.txt
    │   ├── doc_02.txt
    │   ├── doc_03.txt
    │   ├── doc_04.txt
    │   ├── doc_05.txt
    │   ├── doc_06.txt
    │   ├── doc_07.txt
    │   └── doc_08.txt
    │
    ├── Dockerfile
    ├── graph.py
    ├── ingestion.py
    ├── main.py
    ├── models.py
    ├── prompts.py
    ├── retrieval.py
    └── README.md

The local `chroma_db/` directory is generated during ingestion and is excluded from Git.

---

## 3. Knowledge Base

The assistant uses eight Zepto policy documents covering:

1. Delivery Policy
2. Returns & Refunds
3. Membership Tiers
4. Order Tracking
5. Order Cancellation Policy
6. Damaged or Missing Items
7. Gift Cards
8. Customer Support Hours

Each document is stored as a separate text file in the `docs/` directory.

---

## 4. Document Ingestion

`ingestion.py` loads all `.txt` files from the `docs/` directory.

For every document:

1. Read the document text.
2. Generate an embedding using `all-MiniLM-L6-v2`.
3. Store the document ID, text, and embedding in ChromaDB.

ChromaDB is configured to use cosine similarity for vector retrieval.

Run ingestion from the project root:

    python support_assistant/ingestion.py

Expected output:

    Documents ingested successfully.

---

## 5. Retrieval

`retrieval.py` is responsible for searching the vector database.

The user query is converted into an embedding using the same Sentence Transformer model used during ingestion.

ChromaDB then retrieves the top 3 most relevant documents using cosine similarity.

The retrieval function returns:

- Retrieved document texts
- Retrieved document IDs

---

## 6. LangGraph Workflow

The workflow is implemented in `graph.py`.

### Intent Classification

The current mock mode checks policy-related keywords such as:

- delivery
- return
- refund
- membership
- tracking
- cancel
- gift card
- support hours

Policy-related questions are routed to retrieval.

Other questions are routed to a direct response.

### Retrieval and Answer Generation

For policy questions, the workflow is:

    Query
      ↓
    Embedding
      ↓
    ChromaDB
      ↓
    Top 3 Documents
      ↓
    Mock Answer

The current mock response uses the most relevant retrieved document to produce a deterministic answer.

---

## 7. Prompt Template

`prompts.py` contains the structured RAG prompt template.

The prompt defines:

- Assistant role
- Retrieved-context restriction
- Task
- Output format
- Answer length
- Negative constraint against hallucination
- Few-shot example
- Retrieved context
- User query

The current local implementation uses deterministic mock generation. The prompt is prepared for the generation layer rather than requiring an external paid LLM service.

---

## 8. FastAPI

The API is implemented in `main.py`.

Start the server:

    python support_assistant/main.py

The API runs on:

    http://127.0.0.1:8000

FastAPI documentation is available at:

    http://127.0.0.1:8000/docs

---

## 9. API Endpoint

### POST `/ask`

Request:

    {
      "query": "What is the delivery fee for orders below INR 149?"
    }

Example PowerShell request:

    Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method Post -ContentType "application/json" -Body '{"query":"What is the delivery fee for orders below INR 149?"}'

Example response:

    {
      "answer": "Based on the retrieved context: Delivery Policy...",
      "sources": [
        "doc_01"
      ],
      "confidence": 1.0
    }

The exact retrieved source ordering may vary depending on the query.

---

## 10. Non-Policy Questions

The current assistant is restricted to Zepto policy questions.

For example:

    {
      "query": "What is the capital of India?"
    }

The assistant returns:

    I can only answer questions about Zepto policies right now.

---

## 11. Response Schema

The API response contains:

- `answer`
- `sources`
- `confidence`

The `confidence` value is constrained to the range:

    0.0 - 1.0

---

## 12. Environment Configuration

The application uses:

    MOCK_LLM=1

by default.

This enables the deterministic local mock implementation.

No external LLM API key is required for the current implementation.

A real LLM generation path is not implemented in the current version.

---

## 13. Docker

The Dockerfile is configured to use the root-level `requirements.txt`.

Build the image from the repository root:

    docker build -f support_assistant/Dockerfile -t zepto-support-assistant .

Run the container:

    docker run -p 7860:7860 zepto-support-assistant

The API will be available at:

    http://127.0.0.1:7860

Swagger documentation:

    http://127.0.0.1:7860/docs

---

## 14. Dependencies

The project uses one consolidated `requirements.txt` at the repository root.

Support Assistant dependencies include:

- `chromadb`
- `sentence-transformers`
- `langgraph`
- `fastapi`
- `uvicorn`
- `pydantic`

---

## 15. Design Decisions

### Local Vector Database

ChromaDB is used as the vector database so the project can run locally without a paid external vector database.

### Sentence Transformer Embeddings

`all-MiniLM-L6-v2` provides lightweight local text embeddings suitable for the policy corpus.

### Cosine Similarity

ChromaDB is configured with cosine similarity for semantic retrieval.

### LangGraph

LangGraph separates intent classification, retrieval, and answer handling into explicit workflow nodes.

### Mock LLM

The mock mode makes the application deterministic and allows the complete RAG workflow to be demonstrated without requiring an external API key.

### Source Attribution

Retrieved document IDs are returned with every policy answer so the source documents can be identified.

---

## 16. Limitations

The current implementation has the following limitations:

- The LLM generation layer is implemented as a deterministic mock.
- Intent classification currently uses keyword-based rules.
- The knowledge base contains the provided Zepto policy documents only.
- The vector database is generated locally during ingestion.
- The ChromaDB directory is not committed to Git.
- The application does not provide live Zepto order information.

---

## 17. Complete Local Setup

From the repository root:

    python -m venv .venv

Activate the environment on Windows:

    .venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

Ingest the policy documents:

    python support_assistant/ingestion.py

Start the API:

    python support_assistant/main.py

Then open:

    http://127.0.0.1:8000/docs

---

## 18. Module Status

The Support Assistant module provides:

- [x] Policy document ingestion
- [x] Sentence Transformer embeddings
- [x] ChromaDB vector storage
- [x] Cosine similarity retrieval
- [x] Top-3 document retrieval
- [x] LangGraph workflow
- [x] Intent classification
- [x] Mock LLM response
- [x] Source document IDs
- [x] Confidence score
- [x] FastAPI `/ask` endpoint
- [x] Dockerfile
- [x] API testing
- [x] Structured RAG prompt