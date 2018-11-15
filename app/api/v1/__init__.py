from flask import Blueprint
from flask_restful import Api, Resource
from app.api.v1.views import AllOrders, OneOrder, GetOneOrder, UserParcels, OneUser, GetUser

version1 = Blueprint('v1', __name__, url_prefix='/api/v1')

api = Api(version1, catch_all_404s=True)

api.add_resource(OneOrder, '/parcel', strict_slashes=False)
api.add_resource(AllOrders, '/parcels', strict_slashes=False)
api.add_resource(GetOneOrder, '/parcels/<string:order_id>', strict_slashes=False)
api.add_resource(UserParcels, '/users/<string:user_id>/parcels', strict_slashes=False)
api.add_resource(OneUser, '/user', strict_slashes=False)
api.add_resource(GetUser, '/users/<int:user_id>', strict_slashes=False)