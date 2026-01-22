import psycopg2
from psycopg2 import sql

# Simple initialization script for the ARCHIVE-AI database
def setup_database(conn_string):
    try:
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        
        # Read schema.sql
        with open('db/schema.sql', 'r') as f:
            schema_sql = f.read()
        
        cur.execute(schema_sql)
        conn.commit()
        print("Database schema initialized successfully.")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    DB_URL = "host=localhost dbname=archive_ai user=postgres password=secret"
    setup_database(DB_URL)