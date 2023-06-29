from database.models import Post, PostPhoto, PostComment, HashTag, db
from datetime import datetime


def get_all_posts_db():
    posts = Post.query.all()
    if posts:
        return posts
    return False


def get_all_photo_db():
    photos = PostPhoto.query.all()
    if photos:
        return photos
    return False


def get_all_user_photo_db(user_id):
    photos = PostPhoto.query.filter_by(user_id=user_id).all()

    if photos:
        return photos
    return False


def get_exact_photo_db(photo_id):
    photo = PostPhoto.query.filter_by(photo_id=photo_id).first()

    if photo:
        return photo
    return False


def delete_photo_db(photo_id):
    photo = PostPhoto.query.filter_by(photo_id=photo_id).first()

    if photo:
        db.session.delete(photo)
        db.session.commit()
    return False


def get_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    if post:
        return post
    return False


def delete_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()

    if post:
        db.session.delete(post)
        db.session.commit()
    return False


def change_post_text_db(post_id, new_text):
    post = Post.query.filter_by(post_id=post_id).first()

    if post:
        post.post_text = new_text
        post.post_date = datetime.now()
        db.session.commit()
    return False


def add_comment_post_db(post_id, comment_user_id, comment_text):
    post_comment = PostComment.query.filter_by(post_id=post_id).first()
    post_comment.comment_text = comment_text
    post_comment.user_id = comment_user_id
    post_comment.comment_date = datetime.now()
    db.session.commit()


def get_comments_post_db(post_id):
    comments = PostComment.query.filter_by(post_id=post_id).all()

    if comments:
        return comments
    return False


def change_comment_post_db(comment_user_id, comment_id, new_text):
    post_comment = PostComment.query.filter_by(comment_user_id=comment_user_id, comment_id=comment_id).first()

    post_comment.comment_text = new_text
    post_comment.comment_date = datetime.now()
    db.session.commit()
    return post_comment


def delete_comment_post_db(comment_user_id, comment_id):
    post_comment = PostComment.query.filter_by(comment_user_id=comment_user_id, comment_id=comment_id).first()

    db.session.delete(post_comment)
    db.session.commit()


def get_all_hashtag_db(size):
    get_hashtag = HashTag.query.all()

    return get_hashtag[:size]


def get_exact_hashtag_db(hashtag_name):
    get_exact_hashtag = HashTag.filter_by(hashtag_name=hashtag_name).all()
    if get_exact_hashtag:
        return get_exact_hashtag
    return False


def create_post_for_hashtag(post_id, hashtags):
    created_hashtags = []
    for hashtag_name in hashtags:
        new_hashtag_post = HashTag(post_id=post_id, hashtag_name=hashtag_name)
        created_hashtags.append(new_hashtag_post)

    db.session.add_all(created_hashtags)
    db.session.commit()

    return True


# загрузка фото
def post_new_photo_db(user_id, photo_path):
    new_post_photo = PostPhoto(user_id=user_id, photo_path=photo_path)

    db.session.add(new_post_photo)
    db.session.commit()

    return new_post_photo.photo_id


def add_new_post_db(user_id, photo_id, photo_text):
    new_post = Post(user_id=user_id, photo_id=photo_id, photo_text=photo_text)
    db.session.add(new_post)
    db.session.commit()

    return new_post.post_id
