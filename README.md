# Legacy CRM ETL Pipeline (with PII Anonymization)

## Overview

This project is a lightweight ETL pipeline built to extract, transform, and anonymize sensitive customer data from a legacy SQL Server database. It simulates real-world data engineering workflows where personally identifiable information (PII) must be securely handled before downstream use.

The pipeline connects to an existing production-style database, extracts records from the `dbo.Client` table, applies deterministic anonymization to sensitive fields, and outputs a clean dataset.

---

## Problem Statement

Legacy systems often contain sensitive customer data that cannot be safely used in analytics or machine learning workflows without proper transformation. This project demonstrates how to:

- Extract structured data from SQL Server
- Identify and isolate PII fields
- Apply anonymization techniques
- Produce a clean, usable dataset for downstream systems

---

## Tech Stack

- Python 3.13
- SQL Server
- pyodbc
- SHA-256 hashing (Python hashlib)
- CSV export (standard library)

---

## Pipeline Flow
SQL Server (dbo.Client)
↓
Extract Layer (pyodbc)
↓
Transform Layer (PII Anonymization)
↓
Output Layer (CSV / structured dataset)


---

## Key Features

- Secure extraction from SQL Server using Windows Authentication
- Deterministic hashing for identity fields (names, SSN, email)
- Removal of sensitive attributes (phone numbers, income, DOB)
- Modular ETL structure (extract + transform separation)
- Production-style schema handling

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt