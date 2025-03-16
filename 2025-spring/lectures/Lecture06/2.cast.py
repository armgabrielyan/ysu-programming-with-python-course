from typing import TypedDict, cast

class User(TypedDict):
    id: int
    name: str

def get_user_data() -> dict:
    """Simulate getting user data from a database or API"""
    return {"id": 1, "name": "Alice"}

def process_user(user: User) -> str:
    return user["name"]

user = get_user_data()
user = cast(User, user)  # Suppresses type checking error
print(process_user(user))
