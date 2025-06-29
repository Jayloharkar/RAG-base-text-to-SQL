// import React, { useState } from "react";

// const App = () => {
//   const [inputText, setInputText] = useState("");
//   const [responseData, setResponseData] = useState(null); // State to store the response

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await fetch("http://127.0.0.1:8000/echo", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify({ text: inputText }),
//       });

//       if (!response.ok) {
//         throw new Error("Failed to fetch");
//       }

//       const data = await response.json();
//       setResponseData(data); // Set the response data in state
//     } catch (error) {
//       console.error("Error:", error);
//     }
//   };

//   return (
//     <div>
//       <form onSubmit={handleSubmit}>
//         <input
//           type="text"
//           value={inputText}
//           onChange={(e) => setInputText(e.target.value)}
//           placeholder="Enter text"
//         />
//         <button type="submit">Submit</button>
//       </form>

//       {/* Display the response */}
//       {responseData && (
//         <div>
//           <p><strong>Input Query:</strong> {responseData.Query}</p>
//           <p><strong>Generated SQL Query:</strong> {responseData.SQLQuery}</p>
//           <h3>Result:</h3>
//           <table border="1">
//             <thead>
//               <tr>
//                 {Object.keys(responseData.Result[0] || {}).map((key) => (
//                   <th key={key}>{key}</th>
//                 ))}
//               </tr>
//             </thead>
//             <tbody>
//               {responseData.Result.map((row, index) => (
//                 <tr key={index}>
//                   {Object.values(row).map((value, idx) => (
//                     <td key={idx}>{value}</td>
//                   ))}
//                 </tr>
//               ))}
//             </tbody>
//           </table>
//         </div>
//       )}
//     </div>
//   );
// };

// export default App;

import React, { useState } from "react";
import "./App.css";

const exampleQueries = [
  "Total sales in 2020",
  "Find products with quantity less than 10",
  "Show top 5 customers by total purchases",
];

const App = () => {
  const [inputText, setInputText] = useState("");
  const [responseData, setResponseData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleExampleClick = (query) => {
    setInputText(query);
    setResponseData(null);
  };

  const handleClear = () => {
    setInputText("");
    setResponseData(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponseData(null);
    try {
      const response = await fetch("http://127.0.0.1:8000/echo", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: inputText }),
      });

      if (!response.ok) {
        throw new Error("Failed to fetch");
      }

      const data = await response.json();
      setResponseData(data);
    } catch (error) {
      setResponseData({ error: error.message });
    }
    setLoading(false);
  };

  return (
    <div className="main-bg">
            <header className="header">
        <div className="header-flex">
          <img
            src="https://www.i2econsulting.com/_next/image?url=%2Fimages%2Fi2e-Logo_RGB-for-digital-use-1.png&w=256&q=75"
            alt="i2e Consulting Logo"
            className="logo"
          />
          <div className="header-center-text">
            <h1>NL to SQL Assistant</h1>
            <p>Transform natural language into SQL queries</p>
          </div>
        </div>
      </header>
      
      <div className="card input-card">
        <h2>Ask Your Question</h2>
        <p>
          Enter your question in natural language and we'll generate the SQL query for you
        </p>
        <form onSubmit={handleSubmit}>
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="e.g., Show all products with quantity less than 10"
            rows={3}
          />
          <div className="button-row">
            <button type="submit" className="run-btn" disabled={loading || !inputText.trim()}>
              {loading ? "Running..." : "Run Query"}
            </button>
            <button type="button" className="clear-btn" onClick={handleClear}>
              Clear
            </button>
          </div>
        </form>
      </div>

      <div className="results-row">
        <div className="card result-card">
          <h3>Generated SQL</h3>
          <div className="result-content">
            {responseData && responseData.SQLQuery
              ? <pre>{responseData.SQLQuery}</pre>
              : <span className="placeholder">SQL query will appear here</span>}
          </div>
        </div>
        <div className="card result-card">
          <h3>Query Result</h3>
          <div className="result-content">
            {responseData && responseData.Result && Array.isArray(responseData.Result) && responseData.Result.length > 0 ? (
              <table>
                <thead>
                  <tr>
                    {Object.keys(responseData.Result[0]).map((key) => (
                      <th key={key}>{key}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {responseData.Result.map((row, idx) => (
                    <tr key={idx}>
                      {Object.values(row).map((val, i) => (
                        <td key={i}>{val}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <span className="placeholder">
                {responseData && responseData.Result && responseData.Result.length === 0
                  ? "No results found."
                  : "Results will appear here after running a query"}
              </span>
            )}
            {responseData && responseData.error && (
              <div className="error">{responseData.error}</div>
            )}
          </div>
        </div>
      </div>

      <div className="card example-card">
        <h3>Example Queries</h3>
        <p>Click on any example to try it out</p>
        <div className="examples-row">
          {exampleQueries.map((q, idx) => (
            <button
              key={idx}
              className="example-btn"
              onClick={() => handleExampleClick(q)}
            >
              {q}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;