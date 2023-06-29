from flask import Blueprint
from database.postservice import get_comments_post_db, add_comment_post_db, change_comment_post_db, delete_comment_post_db

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')


@comment_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_post_comments(post_id: int):
    exact_comments = get_comments_post_db(post_id)

    if exact_comments:
        return {'status': 1, 'message': exact_comments}
    return {'status': 0, 'message': 'Not found'}


@comment_bp.route('/<int:post_id>/<int:comment_user_id>', methods=['POST'])
def publish_comment(post_id: int, comment_user_id: int, comment_text: str):
    comment = add_comment_post_db(post_id, comment_user_id, comment_text)

    return {'status': 1, 'message': comment}


@comment_bp.route('/<int:comment_id>/<int:comment_user_id>', methods=['PUT'])
def change_comment(comment_id: int, comment_user_id: int, new_text: str):
    comment = change_comment_post_db(comment_user_id, comment_id, new_text)

    if comment:
        return {'status': 1, 'message': comment}
    return {'status': 0, 'message': 'Not found'}


@comment_bp.route('/int:comment_id>/<int:comment_user_id>', methods=['DELETE'])
def delete_comment(comment_id: int, comment_user_id: int):
    comment = delete_comment_post_db(comment_id, comment_user_id)

    if comment:
        return {'status': 1, 'message': 'comment deleted'}
    return {'status': 0, 'message': 'Not found'}
