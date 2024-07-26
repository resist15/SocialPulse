from pydantic import BaseModel

# Request Schemas
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

# Response Schemas
class PostResponse(BaseModel):
    title: str
    content: str
    published: bool
    class Config:
        orm_mode = True
