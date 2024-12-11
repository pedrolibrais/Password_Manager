from app.db.session import SessionLocal
from app.repositories.user_repository import UserRepository
from app.repositories.password_repository import PasswordRepository
from app.services.user_service import UserService
from app.services.password_service import PasswordService

# Criando instâncias de repositórios e serviços
db = SessionLocal()

user_repo = UserRepository(db)
user_service = UserService(user_repo)

password_repo = PasswordRepository(db)
password_service = PasswordService(password_repo)

# Exemplo: Criar usuário
try:
    new_user = user_service.register_user("johndoe", "johndoe@example.com", "hashed_password")
    print(f"User created: {new_user.username}")
except ValueError as e:
    print(e)

# Exemplo: Adicionar senha
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
