from fastapi import FastAPI
from fincoach.fincoach_agent import get_financial_advice

app = FastAPI()

@app.post("/advise")
async def advise(user_input: dict):
    return await get_financial_advice(user_input)