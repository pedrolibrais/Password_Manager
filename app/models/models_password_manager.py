from sqlalchemy import Column, String, TIMESTAMP, Text, ForeignKey, func 
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

class Password(Base):
    __tablename__ = 'passwords'
    id = Column(String(40), primary_key=True)
    user_id = Column(String(40), ForeignKey('users.user_id'), nullable=False)
    site_url = Column(String(255))
    site_alias = Column(String(255))
    username_login = Column(String(255))
    username_email = Column(String(255))
    username_phone = Column(String(20))
    password = Column(String(255))
    key_recovery = Column(String(255))
    notes = Column(Text)
    last_modified = Column(TIMESTAMP, onupdate=func.current_timestamp())
    user = relationship('User', back_populates='passwords')

