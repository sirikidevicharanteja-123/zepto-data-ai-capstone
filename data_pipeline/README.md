# Data Pipeline

## Overview

This folder contains the complete data pipeline developed for this project.

The pipeline follows this workflow:

**Web Scraping → Data Cleaning → SQLite Database → SQL Queries**

The main objective is to collect book data from a website, clean and transform the data, store it in a structured SQLite database, and perform SQL-based analysis.

---

## Pipeline Workflow

```text
Books Website
      ↓
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

---

## Setup / Installation

Install the required Python libraries:

```bash
pip install pandas requests beautifulsoup4
```

---

## Project Files

- `scraper.py` - Collects book data from the website.
- `cleaner.ipynb` - Cleans and transforms the scraped data.
- `database.ipynb` - Creates and manages the SQLite database.
- `queries.ipynb` - Performs SQL queries and analysis.

---

## Data Collection

Book data was collected from the Books to Scrape website using Python.

The scraper uses:

- `requests` to retrieve web pages.
- `BeautifulSoup` to parse the HTML content.
- Category URLs to collect books from different categories.

The collected information includes:

- Book title
- Price
- Rating
- Availability
- Category

## Data Cleaning Decisions

The scraped book data is cleaned and transformed before storing it in the database.

The main cleaning steps include:

- Converting book prices from text to numeric values.
- Converting star ratings into integer values.
- Processing availability information into a structured format.
- Cleaning and preparing category information.
- Preparing the final dataset for SQLite database storage.

---

## Currency Conversion

Book prices are converted from GBP to INR using the fixed project conversion rate:

**1 GBP = 105.50 INR**

The converted price is stored in the `price_inr` column.

---

## Technologies Used

- Python
- Pandas
- Requests
- BeautifulSoup
- SQLite

---

## How to Run

Run the files in the following order:

1. Run `scraper.py` to collect book data from the website.
2. Run `cleaner.ipynb` to clean and transform the scraped data.
3. Run `database.ipynb` to create and populate the SQLite database.
4. Run `queries.ipynb` to perform SQL queries and analysis.