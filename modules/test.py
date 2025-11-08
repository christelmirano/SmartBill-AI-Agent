import gspread
from google.oauth2.service_account import Credentials

# ---------- CONFIG ----------
SERVICE_ACCOUNT_FILE = "/mnt/d/UPLB/smartbill-ai/credentials/service_account.json"  # path to your JSON
SHEET_NAME = "SmartBillData"  # exact sheet name

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# ---------- AUTHORIZE ----------
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# ---------- OPEN SHEET ----------
try:
    sheet = client.open(SHEET_NAME).sheet1
except gspread.SpreadsheetNotFound:
    print(f"Spreadsheet '{SHEET_NAME}' not found. Make sure it exists and is shared with your service account.")
    exit(1)

# ---------- TEST WRITE ----------
try:
    # Example bill row
    new_bill = ["Electricity", 2500, "2025-11-10"]
    
    # Append row to the sheet
    sheet.append_row(new_bill)
    print("Successfully added row to the sheet!")
except Exception as e:
    print(f"Error writing to the sheet: {e}")
