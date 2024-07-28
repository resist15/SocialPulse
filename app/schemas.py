from pydantic import BaseModel, EmailStr
from datetime import datetime

''' Request Schemas'''

# Base Class for Posts
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# Create Post Request
class PostCreate(PostBase):
    pass

# Create User Request
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Auth Request schema
class UserAuth(BaseModel):
    email: EmailStr
    password: str

''' Response Schemas '''

# Post Response Model
class PostResponse(PostBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

# User Response Model
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        from_attributes = True
