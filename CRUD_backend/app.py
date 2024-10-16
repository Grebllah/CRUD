from CRUD_backend import app, api, db
from flask_restful import Resource
from flask import request, make_response
from models import User


class Home(Resource):
    def get(self):
        response_dict = {
            "James'": 'CRUD'
        }
        response = make_response(
            response_dict,
            200,
        )
        return response

api.add_resource(Home, '/')

class Users(Resource):

    def get(self):
        
        response_dict_list = [n.to_dict() for n in User.query.all()]

        response = make_response(
            response_dict_list,
            200,
        )

        return response

    def post(self):
        
        new_record = User (
            id=request.form('id'),
            username=request.form('username'),
            email=request.form('email')
        )

        db.session.add(new_record)
        db.session.commit()

        response_dict = new_record.to_dict()

        response = make_response(
            response_dict,
            201,
        )

        return response

api.add_resource(Users, '/users')

class UserByID(Resource):

    def get(self, id):

        response_dict = User.query.filter_by(id=id).first().to_dict()

        response = make_response(
            response_dict,
            200,
        )

        return response
    
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(user, attr, request.form.get(attr))

        db.session.add(user)
        db.session.commit()

        response_dict = user.to_dict()

        response = make_response(
            response_dict,
            200
        )

        return response

    def delete(self, id):

        record = User.query.filter(User.id == id).first()

        db.session.delete(record)
        db.session.commit()

        response_dict = {"message": "record successfully deleted"}

        response = make_response(
            response_dict,
            200
        )

        return response

api.add_resource(UserByID, '/users/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)