import psycopg2
import pandas as pd
from sqlalchemy import create_engine, inspect
from urllib.parse import quote_plus
from config import DB_CONFIG
 
def test_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Database connection successful!")
        conn.close()
        return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False
 
def get_schema_description():
    try:
        escaped_password = quote_plus(DB_CONFIG["password"])
        connection_string = (
            f"postgresql://{DB_CONFIG['user']}:{escaped_password}@"
            f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        )
        engine = create_engine(connection_string)
        inspector = inspect(engine)
        schema = ""
        with engine.connect():
            for table_name in inspector.get_table_names():
                columns = inspector.get_columns(table_name)
                col_str = ", ".join([f"{col['name']} ({col['type']})" for col in columns])
                schema += f"Table: {table_name}\nColumns: {col_str}\n\n"
        return schema if schema else "No tables found in database"
    except Exception as e:
        return f"Error getting schema: {str(e)}"
 
def run_query(sql):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            cursor.execute(sql)
            if cursor.description:
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                return pd.DataFrame(rows, columns=columns)
            else:
                conn.commit()
                return f"Success: {cursor.rowcount} rows affected."
    except psycopg2.Error as e:
        return f" Database Error: {str(e)}"
    except Exception as e:
        return f" Unexpected Error: {str(e)}"
    finally:
        if 'conn' in locals():
            conn.close()