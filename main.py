from fastapi import FastAPI
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from typing import Annotated

from models.user import User

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

# Get Current User
@app.get("/items")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
  return {"token": token}

# Create a user model
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
  return fake_user_by_token(token)

def fake_user_by_token(token: str) -> User:
  return User(
    email = "john@example.com",
    full_name = "John Doe",
    username = f"{token}fakedecoded"
  )

@app.get("/users/me")
async def read_user_me(current_user: Annotated[User, Depends(get_current_user)]) -> User:
  return current_user
