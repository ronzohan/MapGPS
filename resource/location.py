import datetime
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

        user = User(args['longitude'], args['latitude'], args['upload_time'])
        db.session.add(user)
        db.session.commit()

        return {"message": "Success"}

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('limit', required=False)
        parser.add_argument('upload_time_order', required=False, default="asc")
        parser.add_argument('filter_start_date', required=False, default=datetime.date.today())
        parser.add_argument('filter_end_date', required=False, default=datetime.date.today())

        args = parser.parse_args()

        # if start date and end date are the same, add one day to the end date to
        # have the query date >= TODAY and date <= TOMORROW to get all the queries
        # of from time of 00:00:00 up to 23:59:59
        if args['filter_start_date'] == args['filter_end_date']:
            args['filter_end_date'] = datetime.datetime.strptime(args['filter_end_date'], "%Y-%m-%d") \
                                      + datetime.timedelta(days=1)

        # This will check what will be the ordering of the returned location info
        if args['upload_time_order'] == "asc":
            upload_time_order = User.upload_time.asc()
        elif args['upload_time_order'] == "desc":
            upload_time_order = User.upload_time.desc()
        else:
            upload_time_order = User.upload_time.asc()

        if args['limit'] is not None:
            users = db.session.query(User) \
                .filter(User.upload_time.between(args['filter_start_date'], args['filter_end_date'])) \
                .order_by(upload_time_order).limit(args['limit'])
        else:
            users = db.session.query(User).order_by(upload_time_order).all() \
                .filter(User.upload_time.between(args['filter_start_date'], args['filter_end_date']))

        user_locations = []

        for user in users:
            user_locations.append({
                "latitude": user.latitude,
                "longitude": user.longitude,
                "upload_time": str(user.upload_time)
            })

        return {"message": "Success", "locations": user_locations}
