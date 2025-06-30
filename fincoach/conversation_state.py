from fincoach.user_profile import UserProfile

required_slots = ["age", "income", "goal", "children"]

memory_store = {}  # Replace with session-based memory if needed

def update_profile_with_memory(user_input: dict):
    memory_store.update(user_input)
    missing = [slot for slot in required_slots if slot not in memory_store]
    return memory_store, missing