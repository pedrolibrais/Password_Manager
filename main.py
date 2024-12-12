from app.db.session import SessionLocal, Base, engine
from app.repositories.repositories_password_manager import UserRepository, PasswordRepository
from app.factory import service_factory

db = SessionLocal()
Base.metadata.create_all(bind=engine)

user_repo = UserRepository(db)
user_service = service_factory.UserService(user_repo)

password_repo = PasswordRepository(db)
password_service = service_factory.PasswordService(password_repo)

try:
    new_user = user_service.register_user("johndoe", "johndoe@example.com", "hashed_password")
    print(f"User created: {new_user.username}")
except ValueError as e:
    print(e)

# User_Test = user_service.get_user_by_username("johndoe")
# print(User_Test.email)

try:
    new_password = password_service.add_password(
        user_id=new_user.user_id,
        site_url="https://example.com",
        site_alias="Example",
        username_login="johndoe",
        username_email="johndoe@example.com",
        username_phone="1234567890",
        password="secure_password",
        key_recovery="recovery_key",
        notes="My main account"
    )

    print(f"Password created for site: {new_password.site_alias}")
except:
    print('Usuário Existente')
