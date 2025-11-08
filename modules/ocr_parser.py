import pytesseract
from PIL import Image
from modules.utils import parse_date, parse_amount

def extract_image(file):
    img = Image.open(file)
    text = pytesseract.image_to_string(img)
    
    # Simple example: parse text for demo purposes
    bill_data = {
        "type": "Unknown",
        "amount": parse_amount(text),
        "due_date": parse_date(text)
    }
    return bill_data
