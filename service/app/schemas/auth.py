from pydantic import BaseModel

class SinginInput(BaseModel):
    email: str
    password: str


class SingupInput(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    token: str

class User(BaseModel):
    email: str
    password: str