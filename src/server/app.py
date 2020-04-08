from flask import Flask, g
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)

from server.api.v1 import Answer

"""
Answer URL.

Allowed methods:
- GET (Returns answer with specified id)
- POST (Posts a new answer)
"""
api.add_resource(Answer, '/answer', '/answer/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
