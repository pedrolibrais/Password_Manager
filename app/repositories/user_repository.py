from app.models.user import User
from uuid import uuid4

class UserRepository:
    def __init__(self, db):
        self.db = db

    def create_user(self, username, email, password_hash):
        user = User(
            user_id=str(uuid4()),
            username=username,
            email=email,
            password_hash=password_hash
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email):
        return self.db.query(User).filter(User.email == email).first()
