from langgraph.graph import StateGraph, END
from langchain_core.prompts import PromptTemplate
from fincoach.llm_utils import get_llm
#from fincoach.llm_utils import get_llm
import os
from pydantic import BaseModel
from fincoach.user_profile import UserProfile
from typing_extensions import TypedDict

PROMPT_PATH = os.path.join(os.path.dirname(__file__), "investment_prompt.txt")

class ReasoningState(TypedDict):
    age: int
    income: float
    goal: str
    children: int = 0
    risk_tolerance: str | None = None
    response_content: str
    advice: str

async def run_graph(user_context):
    with open(PROMPT_PATH) as f:
        template = f.read()

    prompt = PromptTemplate.from_template(template)
    llm = get_llm(model="deepseek-r1:8b")

    async def generate_reasoning(state) -> ReasoningState:
        filled_prompt = prompt.format(**state.model_dump())
        response = llm.invoke(filled_prompt)
        return ReasoningState(
            response_content=response.content,
            advice=response.content.split("\n")[-1]
        )

    builder = StateGraph(UserProfile)
    builder.add_node("generate_reasoning", generate_reasoning)
    builder.set_entry_point("generate_reasoning")
    graph = builder.compile()

    result = await graph.ainvoke(user_context)
    return result
