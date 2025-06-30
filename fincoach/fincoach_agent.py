from fincoach.reasoning_chain import run_graph
from fincoach.user_profile import UserProfile
from fincoach.conversation_state import required_slots, update_profile_with_memory

async def get_financial_advice(user_input: dict):
    profile_data, missing = update_profile_with_memory(user_input)
    if missing:
        return {"follow_up_questions": missing}
    profile = UserProfile(**profile_data)
    result = await run_graph(profile.model_dump())
    return {
        "reasoning_steps": result["response_content"].split("\n"),
        "advice": result["advice"]
    }