# Zepto Capstone Project

This repository contains the implementation of the Zepto Capstone Project.

The project is organized into three major modules covering data collection, data processing, analytics, machine learning, and an AI-powered support assistant.

---

## Project Structure

```text
zepto_capstone/
│
├── data_pipeline/
│   ├── scraper.py
│   ├── cleaner.ipynb
│   ├── database.ipynb
│   ├── queries.ipynb
│   ├── data/
│   └── README.md
│
├── analytics/
│   ├── 01_EDA.ipynb
│   ├── 02_modeling.ipynb
│   ├── titanic.csv
│   ├── cleaned_titanic.csv
│   ├── best_titanic_pipeline.joblib
│   └── README.md
│
├── support_assistant/
│   └── README.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Module 1 — Data Pipeline

## Overview

The Data Pipeline module implements an end-to-end data collection and processing workflow.

The pipeline follows:

```text
Web Scraping
     ↓
Raw Data
     ↓
Data Cleaning
     ↓
Cleaned Data
     ↓
SQLite Database
     ↓
SQL Queries and Analysis
```

Book data is collected from the Books to Scrape website, cleaned and transformed, stored in a SQLite database, and analyzed using SQL queries.

## Technologies Used

- Python
- Pandas
- Requests
- BeautifulSoup
- SQLite
- SQL

## Main Components

- `scraper.py` — Collects book data from the website.
- `cleaner.ipynb` — Cleans and transforms the scraped data.
- `database.ipynb` — Creates and manages the SQLite database.
- `queries.ipynb` — Performs SQL queries and analysis.

Detailed documentation:

`data_pipeline/README.md`

## Status

**Completed**

---

# Module 2 — Analytics

The Analytics module performs exploratory data analysis and predictive modeling using the Titanic dataset.

The module includes:

- Exploratory Data Analysis
- Data cleaning
- Missing-value analysis
- Outlier analysis
- Bivariate and multivariate analysis
- Correlation analysis
- Data preprocessing
- Logistic Regression
- Decision Tree
- Random Forest
- Class imbalance analysis
- SMOTE
- Random Forest hyperparameter tuning
- Fare regression
- Model evaluation
- Model persistence using Joblib

Detailed documentation:

`analytics/README.md`

## Main Components

### EDA

```text
analytics/01_EDA.ipynb
```

The notebook contains the complete exploratory data analysis and dataset cleaning workflow.

### Machine Learning

```text
analytics/02_modeling.ipynb
```

The notebook contains classification, class imbalance analysis, Random Forest tuning, fare regression, evaluation, and model persistence.

### Saved Datasets and Model

```text
analytics/titanic.csv
analytics/cleaned_titanic.csv
analytics/best_titanic_pipeline.joblib
```

## Status

**Completed**

---

# Module 3 — Support Assistant

The Support Assistant module will provide an AI-powered support assistant using retrieval-based techniques.

The planned workflow will include:

```text
Support Documents
        ↓
Document Processing
        ↓
Chunking
        ↓
Embeddings
        ↓
Vector Retrieval
        ↓
Relevant Context
        ↓
AI Response
```

The detailed implementation and documentation will be added in:

`support_assistant/README.md`

## Status

**Pending**

---

# Technologies Used

The project currently uses technologies including:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- Joblib
- Requests
- BeautifulSoup
- SQLite
- SQL
- Git
- GitHub

Additional technologies and libraries will be added as required by the Support Assistant module.

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd zepto_capstone
```

Create a virtual environment:

```bash
python -m venv .venv
```

## Windows

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Each module can be executed independently.

## Data Pipeline

Run the components in the following order:

```text
scraper.py
    ↓
cleaner.ipynb
    ↓
database.ipynb
    ↓
queries.ipynb
```

For detailed instructions, refer to:

`data_pipeline/README.md`

---

## Analytics

### Exploratory Data Analysis

Open:

```text
analytics/01_EDA.ipynb
```

### Machine Learning

Open:

```text
analytics/02_modeling.ipynb
```

For detailed Analytics documentation, refer to:

`analytics/README.md`

---

## Support Assistant

The execution instructions will be added after the Support Assistant module is implemented.

---

# Git Workflow

Development is organized using Git branches for module-level development.

The Analytics module was developed on:

```text
feature/analytics
```

Changes are committed incrementally and will be merged into the `main` branch after completion and verification.

---

# Current Project Status

| Module | Status |
|---|---|
| Data Pipeline | Completed |
| Analytics — EDA | Completed |
| Analytics — Machine Learning | Completed |
| Support Assistant | Pending |
| Final Integration | Pending |

---

# Development Progress

```text
Module 1 — Data Pipeline
        ↓
     COMPLETED
        ↓
Module 2 — Analytics
        ↓
     COMPLETED
        ↓
Module 3 — Support Assistant
        ↓
      PENDING
        ↓
Final Integration
```

---

# Author

Developed by **S. Devi Charan Teja Siriki** as part of the Zepto Capstone Project.