from flask import Flask, g
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)

from server.api.v1.dummy import Dummy

"""
Example URL.

Allowed methods:
- GET (Returns "hello world")
"""
api.add_resource(Dummy, '/dummy')

if __name__ == '__main__':
    app.run(debug=True)
