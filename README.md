# Project Overview

This project is a simple text echo application that consists of a FastAPI backend and a React.js frontend. The backend provides an API endpoint that accepts text input and returns the same text, while the frontend allows users to input text and see the echoed response.

## Project Structure

```
text2sql-app
├── backend
│   ├── app.py                # FastAPI application
│   ├── requirements.txt      # Python dependencies
│   └── README.md             # Backend documentation
├── frontend
│   ├── public
│   │   └── index.html        # Main HTML file for React app
│   ├── src
│   │   ├── App.css           # CSS styles for React app
│   │   ├── App.jsx           # Main React component
│   │   ├── index.css         # Global CSS styles
│   │   └── index.jsx         # Entry point for React app
│   ├── package.json          # npm configuration for React app
│   └── README.md             # Frontend documentation
└── README.md                 # Root project documentation
```

## Backend Setup

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```
   python app.py
   ```

4. The API will be available at `http://127.0.0.1:8000/echo`.

## Frontend Setup

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

3. Start the React application:
   ```
   npm start
   ```

4. The application will be available at `http://localhost:3000`.

## Usage

- Enter text in the input field on the frontend and submit the form.
- The echoed text will be displayed below the input field.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.