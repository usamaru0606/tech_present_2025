from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def create_user(db: Session, user_data: UserCreate):
    new_user = User(**user_data.dict(exclude={"passwordConfirm"}))  # `passwordConfirm` を除外
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user