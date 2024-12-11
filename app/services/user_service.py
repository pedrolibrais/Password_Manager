class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def register_user(self, username, email, password_hash):
        existing_user = self.user_repo.get_user_by_email(email)
        if existing_user:
            raise ValueError("User with this email already exists.")
        return self.user_repo.create_user(username, email, password_hash)
