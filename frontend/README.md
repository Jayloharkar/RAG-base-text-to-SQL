# Frontend for the Text2SQL Application

This directory contains the React.js frontend for the Text2SQL application, which interacts with the FastAPI backend.

## Getting Started

To set up and run the frontend application, follow these steps:

1. **Install Dependencies**: Navigate to the `frontend` directory and install the required packages using npm:

   ```
   cd frontend
   npm install
   ```

2. **Run the Application**: Start the development server:

   ```
   npm start
   ```

   This will launch the application in your default web browser at `http://localhost:3000`.

## Features

- A simple form to input text.
- Submits the text to the FastAPI backend and displays the echoed response.

## Folder Structure

- `public/`: Contains the static files, including `index.html`.
- `src/`: Contains the React components and styles.
- `package.json`: Lists the dependencies and scripts for the React application.

## Dependencies

The frontend application is built using React.js and requires the following dependencies:

- `react`
- `react-dom`

Make sure the backend FastAPI application is running to test the full functionality of the frontend.