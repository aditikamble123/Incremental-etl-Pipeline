# Incremental ETL Pipeline with Logging

## Overview
This project implements an **incremental ETL (Extract, Transform, Load) pipeline**
that loads only **new records** into a MySQL data warehouse based on `order_id`.

The pipeline is designed to simulate **real-world production ETL workflows**
where data arrives repeatedly and must be processed safely without duplication.

---

## Business Problem
E-commerce order data is delivered periodically as CSV files.
Reprocessing the entire dataset each time is inefficient and error-prone.

**Goal:**
- Load only **new orders**
- Avoid duplicate data
- Log every ETL run for monitoring and debugging

---

## Architecture

CSV File
↓
Extract (Pandas)
↓
Transform (Incremental Filter)
↓
Load (MySQL via SQLAlchemy)
↓
Logging (etl.log)

yaml
Copy code

---

## Key Features
- Incremental loading using `MAX(order_id)`
- Prevents duplicate data ingestion
- Logging for ETL monitoring
- Chunked inserts for performance
- Secure credential handling using environment variables

---

## Tech Stack
- Python
- Pandas
- MySQL
- SQLAlchemy
- Logging

---

## Project Structure

incremental-etl-pipeline/
│
├── data/
│ └── ecommerce_orders_10k_updated.csv
│
├── etl/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── logs/
│ └── etl.log
│
├── test_etl.py
├── requirements.txt
├── .gitignore
└── README.md

yaml
Copy code

---

## How Incremental Loading Works
1. Query the database to get the latest `order_id`
2. Read the CSV file
3. Filter records where `order_id > max(order_id)`
4. Load only new records into the database
5. Log the execution details

---

## How to Run

### 1. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Set database password
bash
Copy code
set MYSQL_PASSWORD=your_mysql_password
4. Run the ETL pipeline
bash
Copy code
python test_etl.py
Expected Output
First Run
sql
Copy code
Last order_id in DB: 0
Loaded XXXX new records
Incremental ETL completed
Subsequent Runs
pgsql
Copy code
No new records found
Logging
ETL execution details are stored in:

bash
Copy code
logs/etl.log
Example log entries:

pgsql
Copy code
2025-01-14 21:18:02 - INFO - Last order_id in DB: 10000
2025-01-14 21:18:03 - INFO - Loaded 250 new records
