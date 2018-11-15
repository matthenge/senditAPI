"""Version 1 views"""
from flask import jsonify, make_response, request
from flask_restful import Resource
from.parcels_model import Parcels
from.models import UserModel
from flask_restful.reqparse import RequestParser

parcel = Parcels()
users = UserModel()

class OneOrder(Resource):
    """Class for single order endpoints"""
    def __init__(self):
        self.order_parser = RequestParser()
        self.order_parser.add_argument("pickup_location", type=str, required=True, help="Please enter a pickup location")
        self.order_parser.add_argument("destination", type=str, required=True, help="Please enter a destination")
        self.order_parser.add_argument("price", type=str, required=True, help="Invalid price")
        self.order_parser.add_argument("user_id", type=str, required=True, help="invalid user_id")

    def post(self):
        """Create order endpoint"""
        data = self.order_parser.parse_args()
        data = request.get_json()
        pickup_location = data['pickup_location']
        destination = data['destination']
        price = data['price']
        user_id = data['user_id']

        parcel.create_orders(pickup_location, destination, price, user_id)
        return {
            "message": "Order placed Successfully"
        }, 201

class GetOneOrder(Resource):
    """Specific order endpoints"""
    def get(self, order_id):
        """GET specific order"""
        try:
            int(order_id)
        except ValueError:
            return {
                "Error": "Please enter a valid order number"
            }
        one_order = parcel.get_specific_order(order_id)
        return one_order
            
    
    def put(self, order_id):
        """Cancel order"""
        try:
            int(order_id)
        except ValueError:
            return {
                "Error": "Please enter a valid order number"
            }
        cncl = parcel.cancel_order(order_id)
        return {
            "message": cncl
        }, 201

class AllOrders(Resource):
    """Class for all order views"""
    def get(self):
        """Return all orders"""
        all_orders = parcel.get_all_orders()
        return {
            "message": "Success", "Orders": all_orders
        }, 200

class UserParcels(Resource):
    """Class for single user operations"""
    def get(self, user_id):
        """Get all orders by a specific user"""
        try:
            int(user_id)
        except ValueError:
            return {
                "Error": "Please enter a valid user number"
            }
        all_user_orders = parcel.get_orders_by_specific_user(user_id)
        return all_user_orders
        
class OneUser(Resource):
    """Class for single user operations"""
    def post(self):
        """Create user"""
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        email = data['email']
        password = data['password']

        users.add_users(firstname, lastname, username, email, password)
        return{
            "message": "successful registration"
        }, 201

class GetUser(Resource):
    """Get one user"""
    def get(self, user_id):
        """Get a single user"""
        one_user = users.get_one_user(user_id)
        return {
            "message": "user retrieved", "user": one_user
        }, 200
