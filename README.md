# Zepto Data & AI Platform

A modular data and AI platform built as a single capstone project for Zepto-style quick-commerce data workflows.

The project contains three independent modules:

1. Data Pipeline
2. Analytics
3. Support Assistant

Each module has its own implementation and detailed README, while the repository uses one consolidated root `requirements.txt`.

---

## Project Architecture

    Zepto Data & AI Platform
            │
            ├── Data Pipeline
            │      ├── Web Scraping
            │      ├── Data Cleaning
            │      ├── SQLite Database
            │      └── SQL Analysis
            │
            ├── Analytics
            │      ├── EDA
            │      ├── Classification
            │      ├── Imbalance Handling
            │      ├── Hyperparameter Tuning
            │      └── Regression
            │
            └── Support Assistant
                   ├── Policy Documents
                   ├── Embeddings
                   ├── ChromaDB
                   ├── Retrieval
                   ├── LangGraph
                   └── FastAPI

---

## Repository Structure

    zepto_capstone/
    │
    ├── data_pipeline/
    │   ├── scraper.py
    │   ├── cleaner.ipynb
    │   ├── database.ipynb
    │   ├── queries.ipynb
    │   └── README.md
    │
    ├── analytics/
    │   ├── 01_eda.ipynb
    │   ├── 02_modeling.ipynb
    │   ├── cleaned_titanic.csv
    │   ├── titanic.csv
    │   ├── best_titanic_pipeline.joblib
    │   └── README.md
    │
    ├── support_assistant/
    │   ├── docs/
    │   │   ├── doc_01.txt
    │   │   ├── doc_02.txt
    │   │   ├── doc_03.txt
    │   │   ├── doc_04.txt
    │   │   ├── doc_05.txt
    │   │   ├── doc_06.txt
    │   │   ├── doc_07.txt
    │   │   └── doc_08.txt
    │   ├── Dockerfile
    │   ├── graph.py
    │   ├── ingestion.py
    │   ├── main.py
    │   ├── models.py
    │   ├── prompts.py
    │   ├── retrieval.py
    │   └── README.md
    │
    ├── requirements.txt
    ├── .gitignore
    └── README.md

---

# 1. Data Pipeline

The Data Pipeline module implements a complete data collection and storage workflow.

## Workflow

    Web Scraping
        ↓
    Data Cleaning
        ↓
    SQLite Database
        ↓
    SQL Queries
        ↓
    Analysis Results

## Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- SQLite
- SQL

## Main Components

### Web Scraping

`scraper.py` collects book information from the target website.

The scraped information includes fields such as:

- Title
- Price
- Rating
- Availability
- Category

### Data Cleaning

`cleaner.ipynb` performs data cleaning and preprocessing using Pandas.

### Database

`database.ipynb` creates and populates the SQLite database.

### SQL Analysis

`queries.ipynb` performs SQL-based analysis on the stored data.

For complete implementation details, see:

`data_pipeline/README.md`

---

# 2. Analytics

The Analytics module performs exploratory data analysis and machine learning experiments using the Titanic dataset.

## Workflow

    Dataset
       ↓
    Data Cleaning
       ↓
    Exploratory Data Analysis
       ↓
    Feature Processing
       ↓
    Classification
       ↓
    Imbalance Handling
       ↓
    Hyperparameter Tuning
       ↓
    Regression Analysis

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- Joblib

## Classification Models

The module evaluates:

- Logistic Regression
- Decision Tree
- Random Forest

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

## Imbalance Handling

The module compares:

- Baseline classification
- Class-weight balancing
- SMOTE

## Hyperparameter Tuning

GridSearchCV is used for Random Forest hyperparameter tuning.

The selected configuration is stored in the trained pipeline artifact.

## Regression

The Analytics module also includes regression analysis for predicting fare.

Evaluation metrics include:

- MAE
- RMSE
- R²
- Adjusted R²

For complete implementation details and experimental results, see:

`analytics/README.md`

---

# 3. Support Assistant

The Support Assistant is a policy-based Retrieval-Augmented Generation (RAG) service for answering Zepto customer-support questions.

## Workflow

    User Query
        ↓
    FastAPI
        ↓
    LangGraph
        ↓
    Intent Classification
        ↓
    Policy Question?
       /       \
     Yes       No
      ↓         ↓
    Retrieval  Direct Answer
      ↓
    Sentence Transformer
      ↓
    ChromaDB
      ↓
    Top 3 Documents
      ↓
    Mock Answer
      ↓
    Answer + Sources + Confidence

## Technologies

- FastAPI
- LangGraph
- Sentence Transformers
- ChromaDB
- Pydantic
- Uvicorn

## Knowledge Base

The Support Assistant contains eight Zepto policy documents covering:

1. Delivery Policy
2. Returns & Refunds
3. Membership Tiers
4. Order Tracking
5. Order Cancellation Policy
6. Damaged or Missing Items
7. Gift Cards
8. Customer Support Hours

## Embeddings

The project uses:

`all-MiniLM-L6-v2`

for generating document and query embeddings.

## Retrieval

ChromaDB is configured to use cosine similarity.

The retrieval layer returns the top 3 relevant documents.

## LangGraph

LangGraph is used to orchestrate:

- Intent classification
- Retrieval
- Direct response handling
- Answer generation flow

## FastAPI

Start the Support Assistant from the repository root:

    python support_assistant/main.py

The API runs at:

    http://127.0.0.1:8000

Swagger documentation:

    http://127.0.0.1:8000/docs

### Example Request

    {
      "query": "What is the delivery fee for orders below INR 149?"
    }

### Example PowerShell Request

    Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method Post -ContentType "application/json" -Body '{"query":"What is the delivery fee for orders below INR 149?"}'

The response contains:

- Answer
- Retrieved source document IDs
- Confidence score

The current implementation uses a deterministic mock LLM mode and does not require an external LLM API key.

For complete implementation details, see:

`support_assistant/README.md`

---

# 4. Installation

Clone the repository:

    git clone https://github.com/sirikidevicharanteja-123/zepto-data-ai-capstone.git

Move into the project:

    cd zepto_capstone

Create a virtual environment:

    python -m venv .venv

Activate the environment on Windows:

    .venv\Scripts\activate

Install all project dependencies:

    pip install -r requirements.txt

---

# 5. Running the Modules

## Data Pipeline

Follow the detailed instructions in:

`data_pipeline/README.md`

The module contains the scraping, cleaning, database, and SQL notebooks/scripts.

---

## Analytics

Open the notebooks:

    analytics/01_eda.ipynb
    analytics/02_modeling.ipynb

Run the notebooks using Jupyter Notebook or VS Code.

---

## Support Assistant

First ingest the policy documents:

    python support_assistant/ingestion.py

Then start the API:

    python support_assistant/main.py

Open:

    http://127.0.0.1:8000/docs

---

# 6. Docker

The Support Assistant includes a Dockerfile.

Build the image from the repository root:

    docker build -f support_assistant/Dockerfile -t zepto-support-assistant .

Run the container:

    docker run -p 7860:7860 zepto-support-assistant

The API will then be available at:

    http://127.0.0.1:7860

---

# 7. Dependencies

The project intentionally uses one consolidated dependency file:

`requirements.txt`

It contains dependencies required across:

- Data Pipeline
- Analytics
- Support Assistant

This avoids maintaining separate dependency files for individual modules.

---

# 8. Design Decisions

## Modular Structure

The project is divided into three modules so that data engineering, analytics, and AI assistant functionality remain separated.

## Single Repository

All modules are maintained in one GitHub repository as required by the capstone specification.

## Consolidated Requirements

A single root `requirements.txt` is used for the complete project.

## Local-First AI Stack

The Support Assistant uses local embeddings and ChromaDB instead of requiring paid external vector database services.

## Mock LLM

The Support Assistant uses a deterministic mock generation layer so the complete RAG workflow can run locally without requiring an external LLM API key.

---

# 9. Git Workflow

The project uses feature branches for module development.

Example workflow:

    main
      ↓
    feature/analytics
      ↓
    merge into main
      ↓
    feature/support-assistant
      ↓
    merge into main

The Support Assistant was developed on:

`feature/support-assistant`

and then merged into `main`.

---

# 10. Module Status

## Data Pipeline

- [x] Web scraping
- [x] Data cleaning
- [x] SQLite database
- [x] SQL queries
- [x] Module documentation

## Analytics

- [x] Exploratory Data Analysis
- [x] Classification models
- [x] Imbalance handling
- [x] Random Forest tuning
- [x] Regression analysis
- [x] Model artifact
- [x] Module documentation

## Support Assistant

- [x] Policy document ingestion
- [x] Sentence Transformer embeddings
- [x] ChromaDB vector storage
- [x] Cosine similarity retrieval
- [x] Top-3 retrieval
- [x] LangGraph workflow
- [x] Intent classification
- [x] Mock LLM response
- [x] Source document IDs
- [x] Confidence score
- [x] FastAPI `/ask` endpoint
- [x] Dockerfile
- [x] Structured RAG prompt
- [x] Module documentation

---

# 11. Repository

GitHub repository:

https://github.com/sirikidevicharanteja-123/zepto-data-ai-capstone.git
---

# Author

Developed by **S. Devi Charan Teja Siriki** as part of the Zepto Capstone Project.