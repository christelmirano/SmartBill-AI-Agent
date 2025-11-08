import fitz  # PyMuPDF
from modules.utils import parse_date, parse_amount
from modules.ocr_parser import extract_image
from io import BytesIO
from PIL import Image

def extract_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text_content = ""
    
    for page in doc:
        text_content += page.get_text()
    
    if text_content.strip():  # PDF has text
        bill_data = {
            "type": "Unknown",
            "amount": parse_amount(text_content),
            "due_date": parse_date(text_content)
        }
    else:  # Scanned PDF → OCR
        images = [page.get_pixmap().pil_tobytes() for page in doc]
        # For simplicity, use first page image
        image = Image.open(BytesIO(images[0]))
        bill_data = extract_image(image)
    
    return bill_data
