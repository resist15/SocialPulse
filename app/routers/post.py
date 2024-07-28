from .. import models,schemas,oauth2
from fastapi import APIRouter, Response, status, HTTPException, Depends
from typing import List, Optional
from sqlalchemy.orm import Session
from .. database import get_db

router = APIRouter(
    tags=["Posts"],
    prefix="/posts"
)

@router.get('/',response_model=List[schemas.PostResponse])
def get_post_all(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user),limit: int = 10, skip: int = 0,search: Optional[str] = ""):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts

# Create Post Endpoint

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id = current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Get Single Post

@router.get("/{id}",response_model=schemas.PostResponse)
def get_post_single(id: int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    return post

# Delete Post by specific id

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} not found')

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Not Authorized to perform requested action')
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update Post with Specific id

@router.put("/{id}",response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    update_post = post_query.first()
    if update_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} not found')

    if update_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Not Authorized to perform requested action')

    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()

    return post_query.first()


