from pydantic import BaseModel
from datetime import datetime

# Request Schemas
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

# Response Schemas
class PostResponse(PostBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True
