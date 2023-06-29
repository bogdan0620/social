from flask import Blueprint, request
from database.postservice import get_all_posts_db, get_exact_post_db, delete_exact_post_db, add_new_post_db,\
    post_new_photo_db, create_post_for_hashtag, change_post_text_db

post_bp = Blueprint('user_post', __name__, url_prefix='/post')


@post_bp.route('/', methods=['GET'])
def get_all_user_posts():
    all_posts = get_all_posts_db()
    return {'status': 1, 'message': all_posts}


@post_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_post(post_id: int):
    exact_post = get_exact_post_db(post_id)
    if exact_post:
        return {'status': 1, 'message': exact_post}
    else:
        return {'status': 0, 'message': 'not found'}


@post_bp.route('/<int:post_id>', methods=['PUT'])
def change_user_post(post_id: int):
    new_post_text = request.json.get('new_post_text')

    change_post_text_db(post_id, new_post_text)

    return {'status': 1, 'message': 'пост изменен'}


@post_bp.route('/<int:user_id>/<int:post_id>', methods=['DELETE'])
def delete_user_post(user_id: int, post_id: int):
    # user_id?
    delete_post = delete_exact_post_db(user_id)
    if delete_post:
        return {'status': 1, 'message': delete_post}
    else:
        return {'status': 0, 'message': 'Not found'}


@post_bp.route('/upload_post', methods=['POST'])
def create_post(post_text: str, user_id: int):
    file = request.files.get('post_photo', '')
    file.save(f'user_images/{file.filename}')

    hashtags = request.json.get('hashtags')

    new_photo_id = post_new_photo_db(user_id, file.filename)

    new_post_id = add_new_post_db(user_id=user_id, photo_id=new_photo_id, post_text=post_text)

    if hashtags:
        create_post_for_hashtag(new_post_id, hashtags)

    return {'status': 1, 'message': 'пост добавлен'}
