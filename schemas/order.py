from pydantic import BaseModel

class Order(BaseModel):
    orderid: int
    quantity: int
    items: dict
    total: float

class OrderRes(BaseModel):
    orderid: int
    quantity: int
    items: dict
    table: int

class OrderCreation(BaseModel):
    orderid: int
    table: int
    items: dict