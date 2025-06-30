def get_llm(model: str):
    from langchain_ollama import ChatOllama
    return ChatOllama(model=model)