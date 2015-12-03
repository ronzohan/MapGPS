from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from resource.location import Location

app = Flask(__name__)
api = Api(app)


api.add_resource(Location, '/api/location')


if __name__ == '__main__':
    app.run(debug=True)
