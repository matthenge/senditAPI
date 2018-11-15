"""Parcels model"""
from .models import UserModel
orders = []

class Parcels:
    """The Parcels class"""

    def __init__(self):
        self.db = orders
        self.order_status = 'pending'

    def create_orders(self, pickup_location, destination, price, user_id):
        """Create orders"""
        payload = {
            'order_id' : len(orders) + 1,
            'pickup_location': pickup_location, 
            'destination' : destination,
            'status': self.order_status,
            'price' : price, 
            'user_id' : user_id   
        }
        prcl = self.db.append(payload)
        return prcl

    def get_all_orders(self):
        """Return all orders"""
        return self.db

    def get_specific_order(self, order_id):
        """Return a specific order"""
        order = [order for order in self.db if order['order_id'] == order_id]
        if not order:
           return {
               "Error":"Order not found"
           }
        else:
            return order[0]
              

    def get_orders_by_specific_user(self, user_id):
        """Return all orders by a specific user"""
        user_orders = []
        for order in self.db:
            if order['user_id'] == str(user_id):
                user_orders.append(order)
        if not user_orders:
            return{
                "message": "User does not have orders"
            }
        return user_orders

    def cancel_order(self, order_id):
        """Cancel an order"""
        for order in self.db:
            if order['status'] == 'pending':
                order.update({'status': 'cancelled'})
                return {
                    "Message" : "Order cancelled"
                }
            elif order['status'] == 'cancelled':
                return{
                    "Error":"Order has already been cancelled"
                }
            elif order['status'] == 'delivered':
                return{
                    "Error": "Order already delivered"
                }
