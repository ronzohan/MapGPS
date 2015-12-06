from flask_restful import Resource, reqparse
from models.shared_model import db
from models.user import User


class Location(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('longitude', required=True)
        parser.add_argument('latitude', required=True)
        parser.add_argument('upload_time', required=False)

        args = parser.parse_args()

        user = User(args['longitude'],  args['latitude'], args['upload_time'])
        db.session.add(user)
        db.session.commit()

        return {"message": "Success"}

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('limit', required=False)

        args = parser.parse_args()

        if (args['limit'] is not None):
            users = db.session.query(User).limit(args['limit']).order_by(User.upload_time.asc())
        else:
            users = db.session.query(User).order_by(User.upload_time.desc()).all()

        user_locations = []

        for user in users:
            user_locations.append({
                "latitude":user.latitude,
                "longitude":user.longitude,
                "upload_time":str(user.upload_time)
            })


        return {"message": user_locations}