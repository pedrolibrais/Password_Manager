from app.models.models_password_manager import User, Password
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
    
    def get_user_by_username(self, username):
        return self.db.query(User).filter(User.username == username).first()

class PasswordRepository:
    def __init__(self, db):
        self.db = db

    def create_password(self, user_id, site_url, site_alias, username_login, username_email, username_phone, password, key_recovery, notes):
        password_entry = Password(
            id=str(uuid4()),
            user_id=user_id,
            site_url=site_url,
            site_alias=site_alias,
            username_login=username_login,
            username_email=username_email,
            username_phone=username_phone,
            password=password,
            key_recovery=key_recovery,
            notes=notes
        )
        self.db.add(password_entry)
        self.db.commit()
        self.db.refresh(password_entry)
        return password_entry

    def get_passwords_by_user(self, user_id):
        return self.db.query(Password).filter(Password.user_id == user_id).all()