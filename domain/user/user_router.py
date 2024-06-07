from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.user import user_schema, user_crud

router = APIRouter(
    prefix="/api/user",
)


@router.get("/list", response_model=list[user_schema.User])
def user_list(db: Session = Depends(get_db)):
    _user_list = user_crud.get_user_list(db)
    return _user_list


@router.get("/detail/{user_id}", response_model=user_schema.User)
def user_detail(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user(db, user_id=user_id)
    return user


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    user_crud.create_user(db, _user_create)


@router.put("/modify/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def user_modify(user_id: int, _user_modify: user_schema.UserModify, db: Session = Depends(get_db)):
    user_crud.modify_user(db, user_id=user_id, user_modify=_user_modify)


@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def user_delete(user_id: int, db: Session = Depends(get_db)):
    user_crud.delete_user(db, user_id=user_id)