import pyodbc
import csv
from anonymization import anonymize_client


def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=UniteOregon_Prod;"
        "Trusted_Connection=yes;"
    )


def extract_clients(limit=5):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT TOP {limit} *
        FROM dbo.Client
    """)

    rows = cursor.fetchall()

    columns = [col[0] for col in cursor.description]

    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))

    conn.close()
    return results


if __name__ == "__main__":
    data = extract_clients()

    cleaned = [anonymize_client(row) for row in data]

    if cleaned:
        with open("clients_anonymized.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=cleaned[0].keys())
            writer.writeheader()
            writer.writerows(cleaned)

    print("Export complete: clients_anonymized.csv")