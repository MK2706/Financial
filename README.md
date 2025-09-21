# Financial
Financial Document Analyzer – Debug Assignment
Project Overview
The Financial Document Analyzer is an AI-powered system that processes financial documents such as corporate reports, quarterly updates, and investment statements. It extracts insights, performs risk assessments, provides investment recommendations, and generates market insights.
This project was initially provided with deliberate bugs in almost every line of code. The debugging process involved carefully fixing these issues while preserving the structure, naming, and format of the original implementation.
________________________________________
Features
•	Upload and analyze financial documents in PDF format
•	Automated financial analysis using AI models
•	Investment recommendations
•	Risk assessment reports
•	Market insights and strategic suggestions
________________________________________
Project Structure
financial-document-analyzer/
│── main.py        # Entry point for running the project
│── tools.py       # PDF loader, investment tool, risk assessment tool, market insights tool
│── agents.py      # AI agents using the tools
│── task.py        # Task orchestration (defining workflow and interactions)
│── data/
│   └── sample.pdf # Placeholder PDF (replace with actual financial document)
│── requirements.txt
│── README.md
________________________________________
Debugging Summary
Errors Identified
1.	Missing or incorrect import statements.
2.	Incorrect usage of the PDF reading library.
3.	String cleaning logic that caused infinite loops.
4.	Method signatures missing self in class definitions.
5.	Improper use of asynchronous methods without await.
6.	Disconnected workflow between tools, agents, tasks, and the main execution file.
Fixes Implemented
•	Corrected imports and included missing dependencies.
•	Fixed PDF reader logic to properly extract and clean document content.
•	Rewrote text-cleaning operations to avoid infinite iterations.
•	Updated class methods with correct parameters and usage of self.
•	Properly implemented asynchronous methods using async and await.
•	Integrated the workflow so that main.py successfully orchestrates tasks through agents and tools.

