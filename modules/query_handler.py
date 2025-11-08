from modules import sheet_manager
import pandas as pd
import plotly.express as px
from datetime import datetime

def handle_query(query):
    df = sheet_manager.get_all_bills()
    
    response = {"text": "Sorry, I couldn't understand the query."}
    
    # Example simple query handling
    if "due this month" in query.lower():
        now = datetime.now()
        df['due_date'] = pd.to_datetime(df['due_date'], errors='coerce')
        this_month = df[df['due_date'].dt.month == now.month]
        response['text'] = f"You have {len(this_month)} bills due this month, totaling {this_month['amount'].sum():.2f}"
        
        fig = px.bar(this_month, x='type', y='amount', title='Bills Due This Month')
        response['chart'] = fig
    elif "summary" in query.lower():
        df['due_date'] = pd.to_datetime(df['due_date'], errors='coerce')
        summary = df.groupby('type')['amount'].sum().reset_index()
        response['text'] = "Here is your monthly bill summary by type."
        fig = px.pie(summary, names='type', values='amount', title='Monthly Bill Summary')
        response['chart'] = fig
    return response
