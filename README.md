📊 Financial Document Analyzer – Debug Assignment
🚀 Project Overview

The Financial Document Analyzer is an AI-powered system that processes financial documents such as corporate reports, quarterly updates, and investment statements. It extracts insights, performs risk assessment, provides investment recommendations, and generates market insights.

This project was originally full of bugs. Each line of code had at least one error. The debugging process involved fixing these issues while preserving the structure and format of the original code.

🛠️ Features

📂 Upload & Analyze Financial Documents (PDF)

🤖 AI-powered financial analysis

💡 Investment recommendations

⚠️ Risk assessment

📈 Market insights

📁 Project Structure
financial-document-analyzer/
│── main.py        # Entry point for running the project
│── tools.py       # PDF loader, investment tool, risk tool, insights tool
│── agents.py      # AI agents using the tools
│── task.py        # Task orchestration (how agents interact)
│── data/
│   └── sample.pdf # Placeholder PDF (replace with actual financial document)
│── requirements.txt
│── README.md

🐞 Debugging Summary
🔴 Errors Found

Imports were missing or incorrect.

PDF reader class used wrong function calls.

String cleaning logic caused infinite loops.

Class methods were not using self properly.

Async methods were not awaited.

Main execution flow didn’t connect tools, tasks, and agents.

✅ Fixes Applied

Corrected imports and added missing libraries.

Fixed PDF reading using proper loaders.

Cleaned string processing to avoid infinite loops.

Updated class definitions and ensured correct method signatures.

Properly handled async/await usage in tools.

Connected main.py to orchestrate tools → tasks → agents → results.
