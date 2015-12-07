from flask_restful import Api
from flask import Flask
from models.shared_model import db
from resource.location import Location

app = Flask(__name__)
db.init_app(app)

api = Api(app)

@app.before_first_request
def create_database():
     db.create_all()
     db.session.commit()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# load all config files
app.config.from_pyfile('config.py')
api.add_resource(Location, '/api/location')

if __name__ == '__main__':
    app.run(debug=True)
