from app.services.password_service import PasswordService
from app.services.user_service import UserService

class ServiceFactory:
    def __init__(self, user_repo, password_repo):
        self.user_repo = user_repo
        self.password_repo = password_repo

    def create_user_service(self):
        return UserService(self.user_repo)

    def create_password_service(self):
        return PasswordService(self.password_repo)