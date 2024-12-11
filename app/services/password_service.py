class PasswordService:
    def __init__(self, password_repo):
        self.password_repo = password_repo

    def add_password(self, user_id, site_url, site_alias, username_login, username_email, username_phone, password, key_recovery, notes):
        return self.password_repo.create_password(
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

    def list_passwords(self, user_id):
        return self.password_repo.get_passwords_by_user(user_id)
