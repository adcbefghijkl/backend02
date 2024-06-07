import datetime

from pydantic import BaseModel, field_validator


class User(BaseModel):
    id: int
    name: str
    start_date: datetime.datetime
    end_date: datetime.datetime | None = None
    job: str
    salary: int


class UserCreate(BaseModel):
    name: str
    job: str
    salary: int

    @field_validator("name", "job")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v


class UserModify(BaseModel):
    name: str
    job: str
    salary: int

    @field_validator("name", "job")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v