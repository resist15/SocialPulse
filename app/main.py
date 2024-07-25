from fastapi import Depends, FastAPI, Response, status, HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from . import schemas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Get All Posts

@app.get('/posts')
def get_post_all(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

# Create Post Endpoint

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Get Single Post

@app.get("/posts/{id}")
def get_post_single(id: int, db: Session = Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    return post

# Delete Post by specific id

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} not found')
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update Post with Specific id

@app.put("/posts/{id}")
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    update_post = post_query.first()
    if update_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} not found')

    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()

    return post_query.first()
