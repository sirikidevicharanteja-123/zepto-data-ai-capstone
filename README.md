# Zepto Capstone Project

This repository contains the implementation of the Zepto Capstone Project.

The project is organized into three major modules covering data collection, data processing, analytics, machine learning, and an AI-powered support assistant.

---

## Project Structure

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
    │   └── titanic.csv
    │
    ├── support_assistant/
    │
    ├── README.md
    ├── requirements.txt
    └── .gitignore

---

# Module 1 — Data Pipeline

## Overview

The Data Pipeline module implements an end-to-end data collection and processing workflow.

The pipeline follows:

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

Book data is collected from the Books to Scrape website, cleaned and transformed, stored in a SQLite database, and then analyzed using SQL queries.

## Technologies Used

- Python
- Pandas
- Requests
- BeautifulSoup
- SQLite

## Main Components

- `scraper.py` — Scrapes book information from different book categories.
- `cleaner.ipynb` — Cleans and transforms the scraped data.
- `database.ipynb` — Creates and manages the SQLite database.
- `queries.ipynb` — Performs SQL queries and analysis.
- `data/` — Contains the pipeline data files.

Detailed documentation for the Data Pipeline is available in:

`data_pipeline/README.md`

## Status

**Completed**

---

# Module 2 — Analytics

The Analytics module uses the classic Titanic dataset to perform exploratory data analysis.

The EDA workflow is implemented in:

`analytics/01_EDA.ipynb`

The raw Titanic dataset is preserved as:

`analytics/titanic.csv`

---

## Exploratory Data Analysis

The EDA includes:

- Dataset shape, information, and descriptive statistics
- Missing-value analysis
- Missing-value percentage calculation
- Missing-value handling based on defined thresholds
- Age distribution analysis
- Fare distribution analysis
- IQR-based outlier detection
- Fare mean, median, and mode
- Fare skewness analysis
- Survival analysis by sex
- Survival analysis by passenger class
- Survival analysis by sex and passenger class
- Correlation analysis
- Correlation heatmap
- Multivariate analysis
- Z-score standardization sanity check

---

## Dataset Cleaning

The original Titanic dataset contained missing values in:

- `age`
- `embarked`
- `deck`
- `embark_town`

The following decisions were made based on the percentage of missing values:

| Column | Missing % | Decision |
|---|---:|---|
| `age` | 19.87% | Median imputation |
| `embarked` | 0.22% | Drop affected rows |
| `deck` | 77.22% | Drop column |
| `embark_town` | 0.22% | Drop affected rows |

After cleaning:

- Rows: **889**
- Columns: **14**
- Missing values: **0**

The raw Titanic dataset is preserved in `analytics/titanic.csv` as an offline fallback.

---

## Univariate Analysis

Age and Fare distributions were analyzed using histograms and boxplots.

### Age

Using the IQR method:

- Q1 = **22.00**
- Q3 = **35.00**
- IQR = **13.00**
- Lower Bound = **2.50**
- Upper Bound = **54.50**
- Potential Outliers = **65**

### Fare

Using the IQR method:

- Q1 = **7.8958**
- Q3 = **31.00**
- IQR = **23.1042**
- Lower Bound = **-26.7605**
- Upper Bound = **65.6563**
- Potential Outliers = **114**

Fare statistics:

- Mean = **32.0967**
- Median = **14.4542**
- Mode = **8.05**

Since:

    Mean > Median > Mode

the Fare distribution is positively/right-skewed.

---

## Bivariate Analysis

### Survival by Sex

- Female survival rate: **74.04%**
- Male survival rate: **18.89%**

Female passengers had a substantially higher survival rate than male passengers.

### Survival by Passenger Class

- First Class: **62.62%**
- Second Class: **47.28%**
- Third Class: **24.24%**

Higher passenger class was associated with a higher survival rate.

### Survival by Sex and Passenger Class

| Sex | Class | Survival Rate |
|---|---:|---:|
| Female | 1 | 96.74% |
| Female | 2 | 92.11% |
| Female | 3 | 50.00% |
| Male | 1 | 36.89% |
| Male | 2 | 15.74% |
| Male | 3 | 13.54% |

The combination of sex and passenger class shows a strong difference in survival. Female first-class passengers had the highest survival rate, while male third-class passengers had the lowest.

---

## Correlation Analysis

The correlation matrix was calculated using the following six numerical features:

- `survived`
- `pclass`
- `age`
- `sibsp`
- `parch`
- `fare`

The two strongest feature relationships based on absolute correlation were:

- `pclass` ↔ `fare`: **-0.5482**
- `pclass` ↔ `age`: **-0.3365**

The negative correlation between passenger class and fare indicates that the numerical encoding of passenger class is inversely related to fare. The relationship between passenger class and age is weaker but also negative.

---

## Multivariate Analysis

Four different multivariate visualizations were used to investigate survival patterns:

1. Sex + Passenger Class + Survival
2. Age + Survival + Sex
3. Fare + Passenger Class + Survival
4. Age Group + Sex + Survival

These visualizations provide a combined view of the factors associated with Titanic passenger survival.

---

## Standardization Sanity Check

Z-score standardization was performed on `age` and `fare` as an EDA sanity check.

After standardization:

    Mean ≈ 0
    Standard Deviation ≈ 1

The standardized values were used only for the EDA sanity check and are not used directly as the machine-learning preprocessing pipeline.

---

## Analytics Status

**EDA Completed**

Machine learning will be implemented as the next stage of the Analytics module.

---

# Module 3 — Support Assistant

The Support Assistant module will be implemented as the final major module of the project.

The implementation details will be added as development progresses.

## Status

**Pending**

---

# Installation

Clone the repository and install the required dependencies.

    git clone <repository-url>
    cd zepto_capstone

Create a virtual environment:

    python -m venv .venv

### Windows

Activate the virtual environment:

    .venv\Scripts\activate

Install the required dependencies:

    pip install -r requirements.txt

---

# Running the Project

Each module can be executed independently.

## Data Pipeline

Run the Data Pipeline components in the following order:

    scraper.py
        ↓
    cleaner.ipynb
        ↓
    database.ipynb
        ↓
    queries.ipynb

## Analytics

Open the EDA notebook:

    analytics/01_EDA.ipynb

The notebook contains the Titanic dataset loading, cleaning, exploratory analysis, and visualization workflow.

The machine learning workflow will be added as development continues.

## Support Assistant

The execution instructions for the Support Assistant will be added after the module is implemented.

---

# Design Decisions

## Data Pipeline

The Data Pipeline separates web scraping, data cleaning, database operations, and SQL analysis into different components.

This keeps the workflow modular and makes each stage easier to develop, test, and maintain.

## Analytics

The Analytics module uses a single Titanic dataset throughout the EDA workflow.

The raw dataset is preserved as an offline fallback, while the cleaned DataFrame is used for subsequent analysis.

Missing-value handling is based on the percentage of missing observations rather than applying the same strategy to every column.

Machine learning preprocessing will be fitted only on training data to avoid data leakage.

## Support Assistant

The Support Assistant will use a retrieval-based approach so that responses can be grounded in the available support documents.

Detailed design decisions will be documented after implementation.

---

# Git Workflow

Development is organized using Git branches for module-level development.

The Analytics module is being developed on:

    feature/analytics

Changes are committed incrementally and will be merged into the `main` branch after completion and verification.

---

# Current Project Status

| Module | Status |
|---|---|
| Data Pipeline | Completed |
| Analytics — EDA | Completed |
| Analytics — Machine Learning | In Progress |
| Support Assistant | Pending |
| Final Integration | Pending |

---

# Technologies Used

The project currently uses technologies including:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- BeautifulSoup
- Requests
- SQLite
- SQL
- Git
- GitHub

Additional libraries will be added as required by the remaining modules.

---

# Development Progress

The project is being developed incrementally, with each module completed and tested before moving to the next stage.

    Module 1 — Data Pipeline
              ↓
           COMPLETED
              ↓
    Module 2 — Analytics EDA
              ↓
           COMPLETED
              ↓
    Module 2 — Analytics ML
              ↓
           IN PROGRESS
              ↓
    Module 3 — Support Assistant
              ↓
            PENDING
              ↓
        Final Integration

---

# Author

Developed by **S. Devi Charan Teja Siriki** as part of the Zepto Capstone Project.