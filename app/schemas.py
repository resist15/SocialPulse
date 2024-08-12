from typing import Optional
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

class Vote(BaseModel):
    post_id: int
    dir: bool

''' Response Schemas '''

# User Response Model
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class ConfigDict:
        from_attributes = True

class UserResPost(BaseModel):
    id: int
    email: EmailStr
    class ConfigDict:
        from_attributes = True

# Post Response Model
class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner: UserResPost
    class ConfigDict:
        from_attributes = True

class PostOut(BaseModel):
    Post: PostResponse
    likes: int
    class ConfigDict:
        from_attributes = True

''' Token Schema'''
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None
