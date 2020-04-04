from flask_restful import Resource


class Dummy(Resource):
    def get(self):
        return {'message': 'Hello world!'}, 200
