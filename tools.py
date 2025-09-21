# tools.py
import os
import re
import asyncio
from crewai.tools import BaseTool
from crewai_tools import SerperDevTool

# Search tool
search_tool = SerperDevTool()


class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader"
    description: str = "Reads and extracts text from financial PDF documents."

    def _run(self, path: str = "data/sample.pdf") -> str:
        import PyPDF2
        if not os.path.exists(path):
            raise FileNotFoundError(f"PDF file not found at: {path}")
        reader = PyPDF2.PdfReader(path)
        pages = []
        for page in reader.pages:
            text = page.extract_text() or ""
            text = re.sub(r'\n{2,}', '\n', text).strip()
            pages.append(text)
        return "\n".join([pg for pg in pages if pg])

    async def _arun(self, path: str = "data/sample.pdf") -> str:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self._run, path)


class InvestmentTool(BaseTool):
    name: str = "Investment Analysis Tool"
    description: str = "Analyzes financial documents for investment insights."

    def _run(self, financial_document_data: str) -> str:
        cleaned = re.sub(r'\s+', ' ', financial_document_data).strip()
        numbers = re.findall(r"[-+]?\d[\d,]*(?:\.\d+)?", cleaned)
        return f"Investment analysis placeholder — cleaned_length={len(cleaned)}, numeric_tokens_found={len(numbers)}"

    async def _arun(self, financial_document_data: str) -> str:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self._run, financial_document_data)


class RiskTool(BaseTool):
    name: str = "Risk Assessment Tool"
    description: str = "Assesses risk from financial documents."

    def _run(self, financial_document_data: str) -> str:
        cleaned = re.sub(r'\s+', ' ', financial_document_data).strip()
        high_leverage_words = ["debt", "leverage", "loan", "interest"]
        count = sum(1 for w in high_leverage_words if w in cleaned.lower())
        return f"Risk assessment placeholder — naive_risk_indicators={count}, cleaned_len={len(cleaned)}"

    async def _arun(self, financial_document_data: str) -> str:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self._run, financial_document_data)
