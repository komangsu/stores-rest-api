from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="field cannot blank!"
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="field cannot blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'messages': 'user already exists!'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'messages': 'creating user success.'}, 201
