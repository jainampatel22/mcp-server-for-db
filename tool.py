import psycopg2
import os
import json
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DB_URL,sslmode='require')

def createTable():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS model_contexts (
                id SERIAL PRIMARY KEY,
                model_name TEXT NOT NULL,
                "context" JSONB NOT NULL,
                created_at TIMESTAMPTZ DEFAULT now(),
                updated_at TIMESTAMPTZ DEFAULT now()
            );
        """)
        conn.commit()
def delete():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            DROP TABLE IF EXISTS model_contexts
                """)


