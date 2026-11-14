
from sqlalchemy.orm import Session

from backend.app.models.user import User
from backend.app.schemas.user import UserCreate


def create_user(db: Session, user_data: UserCreate):
    new_user = User(
        Username=user_data.username,
        Email=user_data.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.UserID == user_id).first()


def update_user(db: Session, user_id: int, user_data: UserCreate):
    user = get_user_by_id(db, user_id)

    if user is None:
        return None

    user.Username = user_data.username
    user.Email = user_data.email

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)

    if user is None:
        return False

    db.delete(user)
    db.commit()

    return True
