from generate_query import query_llama3
from db_config import run_query, get_schema_description
import pandas as pd

SCHEMA = get_schema_description()
print("text",SCHEMA)
print("Database Schema Loaded!")

import json

def generate_sql(nl_query):
    prompt = f"""
    You are an SQL generator expert, your role is to generate an SQL query for a user's natural language query.
    Given the following database schema:
    {SCHEMA}

    The user asks: "{nl_query}"

    Please generate a SQL query that would answer this question.
    Instructions:
    - Return ONLY the SQL query, nothing else.
    - Do not include any comments or explanations.
    - Ensure the SQL is valid and executable.
    
    SQL Query:
    """
    response = query_llama3(prompt)
    # Parse the response as JSON if it's a string
    try:
        if isinstance(response, str):
            response_json = json.loads(response)
        else:
            response_json = response
        sql = response_json["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Warning: Unexpected response format, using fallback. Error:", e)
        sql = str(response).strip()
    return sql

def sql_to_postgres(sql_query):
    """
    Uses LLM to convert a generic SQL query to PostgreSQL syntax.
    """
    prompt = f"""
    You are an expert in SQL dialects. Convert the following SQL query to valid PostgreSQL syntax.
    Return ONLY the converted PostgreSQL SQL query, nothing else.
    Do NOT include any markdown, code fences, explanations, or comments—just the SQL query as plain text.
    If the query uses functions not available in PostgreSQL (like STRFTIME), replace them with the correct PostgreSQL equivalent (such as TO_CHAR or EXTRACT).
    SQL Query:
    {sql_query}
    """
    response = query_llama3(prompt)
    try:
        if isinstance(response, str):
            response_json = json.loads(response)
        else:
            response_json = response
        postgres_sql = response_json["choices"][0]["message"]["content"].strip()
        # Remove code fences if still present
        if postgres_sql.startswith("```"):
            postgres_sql = postgres_sql.strip("`").replace("sql", "", 1).strip()
        # Optional: Replace common non-Postgres functions
        postgres_sql = postgres_sql.replace("STRFTIME('%Y', date)", "EXTRACT(YEAR FROM date)")
    except Exception as e:
        print("Warning: Unexpected response format in sql_to_postgres, using fallback. Error:", e)
        postgres_sql = str(response).strip()
    return postgres_sql

def handle_query(nl_query):
    print(f"[handle_query] Received NL query: {nl_query}")  # Debug input

    if not nl_query.strip():
        print("[handle_query] Empty query received.")
        return "Please enter a question", "No query to process"

    sql_query = generate_sql(nl_query)
    print(f"[handle_query] Generated SQL: {sql_query}")  # Debug SQL

    if sql_query.startswith("Error:"):
        print(f"[handle_query] SQL generation error: {sql_query}")
        return sql_query, "See SQL output for error"
    
    
    postgres_sql_query = sql_to_postgres(sql_query) 
    result_df = run_query(postgres_sql_query)
    print(f"[handle_query] Query result type: {type(result_df)}")  # Debug result type

    if isinstance(result_df, str):
        print(f"[handle_query] Query execution error: {result_df}")
    else:
        print(f"[handle_query] Query execution returned DataFrame with shape: {result_df.shape}")

    return sql_query, result_df
 