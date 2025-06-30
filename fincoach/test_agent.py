import pytest
from fincoach_agent import FinCoachAgent

def test_ask_returns_response():
    agent = FinCoachAgent()
    response = agent.ask("Should I invest in stocks?", user_profile={"age": 45})
    print('Response: ', response)
    assert "reasoning" in response
    assert "advice" in response 