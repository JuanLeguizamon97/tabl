from models.model import Order as UserOrder
from schemas.order import Order, OrderRes, OrderCreation

class OrderUser():

    def __init__(self, db) -> None:
        self.db = db

    def get_order(self):
        result = self.db.query(UserOrder).all()
        return result

    def get_order_by_id(self, id):
        result = self.db.query(UserOrder).filter(UserOrder.id == id).first()
        return result
    
    def create_order(self, order: UserOrder):
        new_order = UserOrder(**order.model_dump())
        self.db.add(new_order)
        self.db.commit()

class OrderRestaurant():

    def __init__(self, db) ->None:
        self.db = db

    def get_orders(self):
        result = self.db.query(OrderRes).all()
        return result
    
    def get_orders_by_table(self,id):
        result = self.db.query(OrderRes).filter(id).first()
        return result
    
    
