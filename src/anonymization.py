import hashlib
from datetime import date, datetime


def hash_value(value):
    if value is None:
        return None
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()[:12]


def clean_value(value):
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    return value


def anonymize_client(row):
    return {
        "EntityID": row.get("EntityID"),
        "LegacyID": row.get("LegacyID"),

        "FirstName": hash_value(row.get("FirstName")),
        "MiddleName": hash_value(row.get("MiddleName")),
        "LastName": hash_value(row.get("LastName")),

        "Email": hash_value(row.get("Email")),
        "SSN": hash_value(row.get("SSN")),
        "ScanCardID": hash_value(row.get("ScanCardID")),

        "HomePhone": None,
        "WorkPhone": None,
        "CellPhone": None,

        "BirthDate": None,

        "Gender": row.get("Gender"),
        "Race": row.get("Race"),
        "Ethnicity": row.get("Ethnicity"),
        "PrimaryLanguage": row.get("PrimaryLanguage"),

        "CreatedDate": clean_value(row.get("CreatedDate")),
        "CreatedBy": row.get("CreatedBy"),
        "OwnedByOrgID": row.get("OwnedByOrgID"),
        "LastModifiedDate": clean_value(row.get("LastModifiedDate")),
        "LastModifiedBy": row.get("LastModifiedBy"),

        "IsContact": row.get("IsContact"),
        "IsCustody": row.get("isCustody"),
        "DeletedDate": clean_value(row.get("DeletedDate")),

        "X_HouseholdMonthlyIncome": None,
        "X_Rent": None,
        "X_MonthlyIncome": None
    }