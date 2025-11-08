import streamlit as st
from datetime import datetime

# ------------------------------
# Page config and CSS
# ------------------------------
st.set_page_config(page_title="SmartBill AI Agent", layout="wide", initial_sidebar_state="collapsed")

# Load external CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ------------------------------
# Header / Title Card
# ------------------------------
st.markdown(
    """
    <div class="title-card">
        <h1>💡 SmartBill AI Agent</h1>
        <p>Upload your bills (PDF or Image) and ask questions like 'Show me bills due this month' or 'Monthly summary'.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ------------------------------
# Upload Section
# ------------------------------

uploaded_file = st.file_uploader(
    "Upload your bill (PDF or Image)", 
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:
    st.info("🔄 Processing file...")

    # Simulate bill data extraction
    bill_data = {
        "vendor": "Sample Vendor Corp",
        "amount": "$156.99",
        "due_date": "March 15, 2025",
        "description": "Monthly service bill",
        "file_name": uploaded_file.name,
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    st.success("✅ Bill data extracted successfully!")
    st.json(bill_data)
    st.info("💾 Bill saved to database successfully!")

st.divider()

# ------------------------------
# Query Section
# ------------------------------

user_query = st.text_input(
    "Enter your query here (e.g., 'Show me bills due this month')",
    placeholder="Ask about bills, request a summary, or describe what you need..."
)

if user_query:
    st.info("🔍 Analyzing your query...")

    # Simulate response
    response_text = (
        f"Based on your query '{user_query}', I found the following bills due this month "
        "with a total amount of $456.75 from 3 vendors."
    )

    st.subheader("📊 Response:")
    st.write(response_text)
    st.info("📈 Chart data would be displayed here")

st.divider()

# ------------------------------
# Display All Bills
# ------------------------------
if st.checkbox("📋 Show all bills in database"):
    sample_bills = [
        {"Vendor": "Acme Corp", "Amount": "$156.99", "Due Date": "2025-03-15"},
        {"Vendor": "Tech Services", "Amount": "$89.50", "Due Date": "2025-03-20"},
        {"Vendor": "Utilities Plus", "Amount": "$210.26", "Due Date": "2025-03-10"},
    ]
    st.dataframe(sample_bills, use_container_width=True)
