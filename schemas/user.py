from pydantic import BaseModel

class User(BaseModel):
    username: str
    fullname: str | None = None
    email: str
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str
    
class UserCreate(BaseModel):
    username: str
    password: str
    email: str

class UserLogin(BaseModel):
    username: str
    password: str