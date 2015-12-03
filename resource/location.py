from flask_restful import Resource, reqparse
from models.user import User


class Location(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('longitude', required=True)
        parser.add_argument('latitude', required=True)

        args = parser.args()
        user = User(args['longitude', 'latitude'])

        return {"message": "Success"}

    def get(self):
        users = User.query.all()

        return {"message": users}