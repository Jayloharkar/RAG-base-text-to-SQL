# Backend FastAPI Application

This directory contains the FastAPI application that serves as the backend for the text echoing service.

## Requirements

To run the FastAPI application, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

The `requirements.txt` file includes the following dependencies:

- fastapi
- uvicorn

## Running the Application

To start the FastAPI application, run the following command:

```
python app.py
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoint

### POST /echo

This endpoint accepts a JSON payload with the following structure:

```json
{
  "text": "your text here"
}
```

It returns a JSON response with the echoed text:

```json
{
  "output": "your text here"
}
```

## Testing the API

You can test the API using tools like Postman or curl. Here’s an example using curl:

```bash
curl -X POST "http://127.0.0.1:8000/echo" -H "Content-Type: application/json" -d '{"text": "Hello, World!"}'
```

This should return:

```json
{
  "output": "Hello, World!"
}
```