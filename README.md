# Legacy CRM ETL Pipeline (with PII Anonymization)

## Overview

This project is a lightweight ETL pipeline built to extract, transform, and anonymize sensitive customer data from a legacy SQL Server database. It simulates real-world data engineering workflows where personally identifiable information (PII) must be securely handled before downstream use.

The pipeline connects to an existing SQL Server database, extracts records from the `dbo.Client` table, applies deterministic anonymization to sensitive fields, and outputs a clean dataset.

---

## Problem Statement

Legacy systems often contain sensitive customer data that cannot be safely used in analytics or machine learning workflows without proper transformation. This project demonstrates how to:

- Extract structured data from SQL Server
- Identify and isolate PII fields
- Apply anonymization techniques
- Produce a clean dataset for downstream systems

---

## Tech Stack

- Python 3.13
- SQL Server
- pyodbc
- SHA-256 hashing (hashlib)
- CSV export (standard library)

---

## Pipeline Flow

SQL Server (dbo.Client)
        ↓
Extract Layer (pyodbc)
        ↓
Transform Layer (PII Anonymization)
        ↓
Output Layer (CSV file)

---

## Key Features

- Secure extraction using Windows Authentication
- Deterministic hashing for identity fields (names, SSN, email)
- Removal of sensitive attributes (phone numbers, income, DOB)
- Modular ETL structure (extract + transform separation)
- Production-style schema handling

---

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run pipeline
py src/extract.py

### Output
clients_anonymized.csv

---

## Security & Privacy

- All PII fields are hashed or removed
- No raw sensitive data is stored in outputs
- Designed to follow basic data protection principles (GDPR-style anonymization)

Before:
John Smith | 555-1234 | john@email.com

After:
a3f91c... | None | 9b21ff...

---

## Project Structure

legacy-crm-etl-pipeline/
│
├── src/
│   ├── extract.py
│   ├── anonymization.py
│
├── sql/
├── docs/
├── requirements.txt
└── README.md