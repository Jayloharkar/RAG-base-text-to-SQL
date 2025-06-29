from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from query_handler import handle_query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the input model
class TextInput(BaseModel):
    text: str

@app.post("/echo")
async def echo_text(input: TextInput):
    sql_query, result_df = handle_query(input.text)
    # If result_df is a string, it's an error message
    if isinstance(result_df, str):
        return {"Query": input.text, "SQLQuery": sql_query, "Result": [], "Error": result_df}
    result_json = result_df.to_dict(orient="records")
    return {"Query": input.text, "SQLQuery": sql_query, "Result": result_json}

def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()