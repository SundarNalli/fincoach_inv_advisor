# FinCoach: Reasoning-Based Investment Advisor

## Overview
FinCoach is a conversational AI agent that provides personalized investment advice to retail investors. Unlike simple retrieval bots, FinCoach reasons through your financial context, asks clarifying questions, and explains its recommendations step by step.

## Features
- Asks follow-up questions to gather your financial context
- Uses DeepSeek and LangGraph for reasoning and chain-of-thought explanations
- Returns a user profile and tailored investment suggestions
- Provides a Streamlit UI for easy interaction

## Example Conversation
```
User: Should I invest in stocks?
Agent: How old are you? What's your income & savings goal?
User: I'm 45, earning 25L, saving for retirement in 15 years.
Agent:
  Reasoning: Mid-age, decent income, long-term horizon → moderate risk
  Advice: Consider hybrid mutual funds or blue-chip ETFs.
```


## Setup & Installation
1. **Clone the repository**
2. **Install dependencies** (from project root):
   ```bash
   pip install -r fincoach/requirements.txt
   ```
3. **(Optional) Set up a virtual environment**

## Running the FastAPI Backend
From the project root, run:
```bash
uvicorn fincoach.main:app --reload
```
- The API will be available at http://127.0.0.1:8000
- Interactive docs: http://127.0.0.1:8000/docs

## Running the Streamlit UI
In a new terminal, run:
```bash
streamlit run fincoach/ui/app.py
```
- Enter your investment question and interact with the agent.

## Running Tests
```bash
pytest fincoach/tests/
```

## Notes
- Ensure all subdirectories have `__init__.py` files for proper imports.
- DeepSeek and LangGraph integration require appropriate API keys or local models (see `llm_utils.py`).

---

**FinCoach is a work in progress. Contributions and feedback are welcome!** 