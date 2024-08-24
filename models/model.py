from config.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Float

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique= True)
    useremail = Column(String(80), unique=True)
    password = Column(Text)
    is_active = Column(Boolean, default=False)

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    restaurantname = Column(String(50), unique=True)
    restaurantemail = Column(String(80), unique=True)
    password = Column(Text)
    address = Column(String(250))
    is_active = Column(Boolean, default=False)

class Order(Base):
    __tablename__ = 'orders'

    id= Column(Integer, primary_key=True)
    quantity = Column(Integer)
    #Pending to create the items list, link to resturant database(restaurant id and restaurant menu), and user id

class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True)
    #Pending linked to the restaurant and items

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    price = Column(Float)
    currency = Column(String)

    #Pending to add to menus and orders