from flask import Blueprint
from database.postservice import get_all_hashtag_db, get_exact_hashtag_db


hashtag_bp = Blueprint('hashtag', __name__, url_prefix='/hashtag')


@hashtag_bp.route('/', methods=['GET'])
def get_hashtags(size: int):
    get_all_hashtags = get_all_hashtag_db(size)

    if get_all_hashtags:
        return {'status': 1, 'message': get_all_hashtags}
    return {'status': 0, 'message': 'Not found'}


# Получить определенный хэштег
@hashtag_bp.route('/<string:hashtag_name>', methods=['GET'])
def get_exact_hashtag(hashtag_name: str):
    hashtag = get_exact_hashtag_db(hashtag_name)

    if hashtag:
        return {'status': 1, 'message': hashtag}
    return {'status': 0, 'message': "Not found"}
