from dateutil.parser import parse
import re

def parse_date(text):
    try:
        return parse(text, fuzzy=True).date()
    except:
        return None

def parse_amount(text):
    match = re.search(r"(\d+[\.,]?\d*)", text.replace(",", ""))
    if match:
        return float(match.group(1))
    return 0.0
