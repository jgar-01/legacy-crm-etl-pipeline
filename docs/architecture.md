# ARCHITECTURE

## ETL Pipeline Architecture

SQL Server Database (dbo.Client)
          |
          |  pyodbc connection
          ↓
Python Extract Layer (extract.py)
          |
          |  convert rows → dict
          ↓
Transform Layer (anonymization.py)
          |
          |  SHA-256 hashing + field removal
          ↓
Output Layer
   ├── CSV export (clients_anonymized.csv)
   └── Python dictionary output

---

## Components

### Extract Layer
- Connects to SQL Server
- Executes SELECT queries
- Converts rows into dictionaries

### Transform Layer
- Hashes PII fields using SHA-256
- Removes sensitive data (SSN, phones, income)
- Preserves safe metadata

### Output Layer
- Writes anonymized CSV
- Outputs structured dataset

---

## Data Handling Rules

### Removed or hashed
- FirstName / LastName
- SSN
- Email
- Phone numbers
- Financial data

### Retained
- EntityID
- Created/Modified timestamps
- Non-identifying demographic codes

---

## Design Principles

- Separation of extract / transform
- Deterministic anonymization
- Minimal dependencies
- Real-world SQL schema handling

---

## Future Improvements

- Add database load step (warehouse table)
- Incremental extraction (CDC logic)
- Logging and error handling
- Docker containerization
- Airflow scheduling