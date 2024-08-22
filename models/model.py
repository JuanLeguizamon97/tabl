from config.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean,ForeignKey

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique= True)
    useremail = Column(String(80), unique=True)
    password = Column(Text)
    is_active = Column(Boolean, default=False)