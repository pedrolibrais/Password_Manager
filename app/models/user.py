from sqlalchemy import Column, String, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(String(40), primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    passwords = relationship('Password', back_populates='user')
