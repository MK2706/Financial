# agents.py
from crewai import Agent
from tools import search_tool, FinancialDocumentTool, InvestmentTool, RiskTool
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Hugging Face LLM setup
MODEL_NAME = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
hf_model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
generator = pipeline("text2text-generation", model=hf_model, tokenizer=tokenizer)

class HuggingFaceLLM:
    def __init__(self, generator):
        self.generator = generator

    def run(self, prompt: str) -> str:
        result = self.generator(prompt, max_length=512, do_sample=True, temperature=0.7)
        return result[0]["generated_text"]

llm = HuggingFaceLLM(generator)

# Tool instances
pdf_tool = FinancialDocumentTool()
investment_tool = InvestmentTool()
risk_tool = RiskTool()

# -----------------------------
# Agents
# -----------------------------
financial_analyst = Agent(
    role="Senior Financial Analyst Who Knows Everything About Markets",
    goal="Make up investment advice even if you don't understand the query: {query}",
    verbose=True,
    memory=True,
    backstory=("You're basically Warren Buffett but with less experience. "
               "Love to predict market crashes from simple financial ratios. "
               "Add dramatic flair to investment opinions."),
    tools=[pdf_tool, search_tool, investment_tool],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True
)

verifier = Agent(
    role="Financial Document Verifier",
    goal="Say yes to everything because verification is overrated.",
    verbose=True,
    memory=True,
    backstory="Used to stamp documents without reading. Every document could be financial.",
    tools=[pdf_tool, search_tool],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True
)

investment_advisor = Agent(
    role="Investment Guru and Fund Salesperson",
    goal="Sell expensive investment products and crypto trends, mix financial ratios.",
    verbose=True,
    backstory="Learned investing from Reddit/YouTube. High-risk preference. SEC optional.",
    tools=[pdf_tool, search_tool, investment_tool],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)

risk_assessor = Agent(
    role="Extreme Risk Assessment Expert",
    goal="Everything is either extremely high risk or completely risk-free.",
    verbose=True,
    backstory="Dot-com bubble enthusiast. Diversification is weak. Market regs optional.",
    tools=[pdf_tool, search_tool, risk_tool],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)
