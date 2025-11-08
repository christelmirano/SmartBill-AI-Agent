# modules/sheet_manager.py

import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SERVICE_ACCOUNT_FILE = "/mnt/d/UPLB/smartbill-ai/credentials/service_account.json"
SHEET_NAME = "SmartBillData"

# Use both scopes for Sheets + Drive access (gspread needs Drive to find sheets)
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# ---------- AUTH ----------
try:
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
except FileNotFoundError:
    raise FileNotFoundError(f"Service account JSON not found at {SERVICE_ACCOUNT_FILE}")
except Exception as e:
    raise Exception(f"Error authorizing Google Sheets client: {e}")

# ---------- OPEN SHEET ----------
try:
    sheet = client.open(SHEET_NAME).sheet1
except gspread.SpreadsheetNotFound:
    print(f"Spreadsheet '{SHEET_NAME}' not found. Please create it and share with your service account email.")
    sheet = None
except gspread.exceptions.APIError as e:
    raise Exception(f"Google Sheets API error: {e}")

# ---------- FUNCTIONS ----------
def add_bill(bill_data: dict):
    """
    Append a bill to the Google Sheet.
    Expected keys: 'type', 'amount', 'due_date'
    """
    if sheet is None:
        print("Cannot add bill: sheet not available.")
        return

    row = [
        bill_data.get("type", ""),
        bill_data.get("amount", 0),
        str(bill_data.get("due_date", ""))
    ]
    try:
        sheet.append_row(row)
        print("Bill added successfully.")
    except Exception as e:
        print(f"Error adding bill: {e}")

def get_all_bills() -> pd.DataFrame:
    """
    Retrieve all bills as a DataFrame.
    """
    if sheet is None:
        print("Cannot retrieve bills: sheet not available.")
        return pd.DataFrame(columns=["type", "amount", "due_date"])

    try:
        records = sheet.get_all_records()
        df = pd.DataFrame(records)
        if "amount" in df.columns:
            df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
        if "due_date" in df.columns:
            df["due_date"] = pd.to_datetime(df["due_date"], errors="coerce")
        return df
    except Exception as e:
        print(f"Error retrieving bills: {e}")
        return pd.DataFrame(columns=["type", "amount", "due_date"])
