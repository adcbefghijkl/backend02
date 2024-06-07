from datetime import datetime
from models import User
from sqlalchemy.orm import Session

from domain.user.user_schema import UserCreate, UserModify

def get_user_list(db: Session):
    user_list = db.query(User).order_by(User.start_date.desc()).all()
    return user_list


def get_user(db: Session, user_id: int):
    user = db.query(User).get(user_id)
    return user


def create_user(db: Session, user_create: UserCreate):
    db_user = User(name=user_create.name, start_date=datetime.now(), job=user_create.job, salary=user_create.salary)

    db.add(db_user)
    db.commit()


def modify_user(db: Session, user_id: int, user_modify: UserModify):
    db_user = db.query(User).get(user_id)
    db_user.name = user_modify.name
    db_user.job = user_modify.job
    db_user.salary = user_modify.salary

    db.commit()


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).get(user_id)
    db.delete(db_user)
    db.commit()