from app.models.password import Password
from uuid import uuid4

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
