from flask import Blueprint, request
from flask_restx import Resource, Api, fields
from database.userservice import register_user_db, get_exact_user_db, get_all_users_db, delete_user_db
from database.postservice import add_comment_post_db, change_comment_post_db, delete_comment_post_db, get_comments_post_db

swagger_bp = Blueprint('swagger', __name__, url_prefix='/docs')
api = Api(swagger_bp)

model_user = api.model('registration', {'username': fields.String,
                                        'first_name': fields.String,
                                        'last_name': fields.String,
                                        'email': fields.String,
                                        'birthday': fields.String,
                                        'register_date': fields.Date})

user_id_field = api.model('user_id', {'user_id': fields.Integer})


model_post_comment = api.model('add_comment', {'comment_text': fields.String,
                                               'comment_date': fields.Date})

post_id_field = api.model('post_id', {'post_id': fields.Integer})

comment_post_id_field = api.model('comment_id', {'comment_id': fields.Integer})


@api.route('/test-user')
class TestSwagger(Resource):
    def get(self):
        all_users = get_all_users_db()
        return {'message': all_users}


@api.route('/')
class UserService(Resource):
    @api.expect(user_id_field)
    def get(self):
        response = request.json
        user_id = response.get('user_id')
        exact_users = get_exact_user_db(user_id)
        return {'message': exact_users}

    @api.expect(user_id_field)
    def delete(self):
        response = request.json
        user_id = response.get('user_id')
        deleted_user = delete_user_db(user_id)
        return {'message': deleted_user}

    @api.expect(model_user)
    def post(self):
        response = request.json
        new_user = register_user_db(**response)
        return {'status': 'Registered'}


@api.route('/')
class PostCommentService(Resource):
    @api.expect(comment_post_id_field)
    def post(self):
        response = request.json
        post_id = response.get('post_id')
        user_id = response.get('user_id')
        new_comment = add_comment_post_db(post_id, user_id, model_post_comment)
        return {'status': 'Comment added'}

    def get(self):
        response = request.json
        post_id = response.get('post_id')
        all_comments = get_comments_post_db(post_id)
        return {'message': all_comments}

    def put(self):
        response = request.json
        user_id = response.get('user_id')
        comment_id = response.get('comment_id')
        change_comment = change_comment_post_db(user_id, comment_id, new_text)
        return {'message': change_comment}

    def delete(self):
        response = request.json
        user_id = response.get('user_id')
        comment_id = response.get('comment_id')
        deleted_comment = delete_comment_post_db(user_id, comment_id)
        return {'status': 'Comment deleted'}
