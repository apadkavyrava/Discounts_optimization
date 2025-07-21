import os
import pandas as pd
from sqlalchemy import create_engine, text

def load_data(connection_url):
    engine = create_engine(connection_url)
    query = text("""
        SELECT
            o.USER_ID,
            o.CREATED_AT,
            o.TOTAL_COST_PENNIES,
            o.TOTAL_COST_PRE_DISCOUNT_PENNIES,
            e.SENT_AT,
            e.OPENED_EMAIL
        FROM orders AS o
        LEFT JOIN emails_sent AS e
               ON o.USER_ID = e.USER_ID
    """)

    with engine.connect() as conn:
        data = pd.read_sql_query(
            sql=query,
            con=conn,
        )

    return data
