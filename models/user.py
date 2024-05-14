from pydantic import BaseModel

class User(BaseModel):
  email: str | None = None
  username: str
  full_name: str | None = None
  disabled: bool | None = None
