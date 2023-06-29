from flask import Blueprint
from database.userservice import get_all_users_db, get_exact_user_db, delete_user_db, register_user_db, check_user_db


user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/', methods=['GET'])
def get_all_users():
    all_users = get_all_users_db()

    return {'status': 1, 'message': all_users}


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_exact_user(user_id: int):
    exact_user = get_exact_user_db(user_id)

    if exact_user:
        return {'status': 1, 'message': exact_user}
    return {'status': 0, 'message': 'Not found'}


@user_bp.route('/<int:user_id>', methods=['PUT'])
def change_user_info(user_id: int):
    return {'message': 'hello'}


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_exact_user(user_id: int):
    delete_user = delete_user_db(user_id)

    if delete_user:
        return {'status': 1, 'message': 'user deleted'}
    return {'status': 0, 'message': 'Not found'}
