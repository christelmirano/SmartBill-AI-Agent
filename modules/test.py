import gspread
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT_FILE = "/mnt/d/UPLB/smartbill-ai/credentials/service_account.json"
SHEET_NAME = "SmartBillData"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

try:
    sheet = client.open(SHEET_NAME).sheet1
    print("✅ Connected successfully!")
    print("Sheet title:", sheet.title)
except Exception as e:
    print("❌ Connection failed:", e)
