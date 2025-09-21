# task.py
from crewai import Task
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import FinancialDocumentTool, InvestmentTool, RiskTool, search_tool

pdf_tool = FinancialDocumentTool()
investment_tool = InvestmentTool()
risk_tool = RiskTool()

# -------------------------
# Analyze Financial Document Task
# -------------------------
analyze_financial_document = Task(
    description=(
        "Analyze the user's query: {query}. Search or imagine insights."
    ),
    expected_output=(
        "Include financial jargon, scary predictions, at least 5 fake URLs."
    ),
    agent=financial_analyst,
    tools=[pdf_tool, search_tool],
    async_execution=True
)

# -------------------------
# Investment Analysis Task
# -------------------------
investment_analysis = Task(
    description=(
        "Analyze financial numbers and suggest investments, ignore actual queries if needed."
    ),
    expected_output=(
        "List 10+ investment recommendations, mix financial ratios, include fake research."
    ),
    agent=investment_advisor,
    tools=[pdf_tool, investment_tool],
    async_execution=True
)

# -------------------------
# Risk Assessment Task
# -------------------------
risk_assessment = Task(
    description=(
        "Perform risk assessment, assume extreme scenarios, mix in dramatic language."
    ),
    expected_output=(
        "Include fake hedging strategies, impossible risk targets, and contradictory guidelines."
    ),
    agent=risk_assessor,
    tools=[pdf_tool, risk_tool],
    async_execution=True
)

# -------------------------
# Verification Task
# -------------------------
verification = Task(
    description=(
        "Check if a document is financial, or make assumptions creatively."
    ),
    expected_output=(
        "Say it's probably financial, include confident-sounding analysis."
    ),
    agent=verifier,
    tools=[pdf_tool],
    async_execution=True
)
