from flask import Blueprint, request
from database.postservice import get_all_photo_db, delete_photo_db, get_all_user_photo_db, get_exact_photo_db,\
    post_new_photo_db

photo_bp = Blueprint('photo', __name__, url_prefix='/photo')


# get all photos
@photo_bp.route('/', methods=['GET'])
def get_all_photo():
    all_photos = get_all_photo_db()

    if all_photos:
        return {'status': 1, 'message': all_photos}
    return {'status': 0, 'message': 'Not found'}


# publishing photo
@photo_bp.route('/', methods=['POST'])
def publish_photo(user_id: int):
    # get photo from front
    file = request.files.get('image', '')
    file.save('user_images/' + file.filename)

    new_photo = post_new_photo_db(user_id, file.filename)

    return {'status': 1, 'message': 'фото добавлено'}


# get only one photo
@photo_bp.route('/<int:user_id>', methods=['GET'])
def get_exact_user_photos(user_id: int):
    all_user_photo = get_all_user_photo_db(user_id)

    if all_user_photo:
        return {'status': 1, 'message': all_user_photo}
    return {'status': 0, 'message': 'Not found'}


# get user's photo
@photo_bp.route('/<int:photo_id>', methods=['GET'])
def get_exact_photo(photo_id: int):
    exact_photo = get_exact_photo_db(photo_id)

    if exact_photo:
        return {'status': 1, 'message': exact_photo}
    return {'status': 0, 'message': 'Not found'}


# change photo info
@photo_bp.route('/<int:user_id>/<int:photo_id>', methods=['PUT'])
def change_user_photo(photo_id: int, user_id: int):
    return {'status': 1, 'message': 'changed'}


# delete photo
@photo_bp.route('/int:user_id/<int:photo_id>', methods=['DELETE'])
def delete_user_photo(user_id: int, photo_id: int):
    delete_photo = delete_photo_db(user_id, photo_id)

    if delete_photo:
        return {'status': 1, 'message': delete_photo}
    return {'status': 0, 'message': 'Not found'}
