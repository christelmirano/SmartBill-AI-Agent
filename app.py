import streamlit as st
from modules import ocr_parser, pdf_parser, sheet_manager, query_handler
import pandas as pd

st.set_page_config(page_title="SmartBill AI Agent", layout="wide")
st.title("💡 SmartBill AI Agent")
st.write("Upload your bills (PDF or Image) and ask questions like 'Show me bills due this month' or 'Monthly summary'.")

# --- Bill Upload Section ---
st.header("1️⃣ Upload Bill")
uploaded_file = st.file_uploader("Upload your bill (PDF or Image)", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    st.info("Processing file...")
    
    if uploaded_file.type == "application/pdf":
        bill_data = pdf_parser.extract_pdf(uploaded_file)
    else:
        bill_data = ocr_parser.extract_image(uploaded_file)
    
    if bill_data:
        st.success("✅ Bill data extracted successfully!")
        st.json(bill_data)
        
        sheet_manager.add_bill(bill_data)
        st.info("Bill saved to Google Sheets successfully!")
    else:
        st.error("❌ Could not extract bill data. Try another file.")

# --- Query Section ---
st.header("2️⃣ Ask About Your Bills")
user_query = st.text_input("Enter your query here (e.g., 'Show me bills due this month')")

if user_query:
    response = query_handler.handle_query(user_query)
    
    st.subheader("Response:")
    st.write(response.get('text', 'No response available.'))
    
    if 'chart' in response:
        st.plotly_chart(response['chart'], use_container_width=True)

# --- Optional: Display All Bills ---
if st.checkbox("Show all bills in Google Sheets"):
    df_all = sheet_manager.get_all_bills()
    st.dataframe(df_all)
