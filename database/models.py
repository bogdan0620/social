from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    register_date = db.Column(db.DateTime)


class Password(db.Model):
    __tablename__ = 'user_passwords'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    password = db.Column(db.String, nullable=False)

    user_fk = db.relationship(User)


class PostPhoto(db.Model):
    __tablename__ = 'user_photos'
    photo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    photo_path = db.Column(db.String, nullable=False)

    user_fk = db.relationship(User)


class Post(db.Model):
    __tablename__ = 'user_post'
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    photo_id = db.Column(db.Integer, db.ForeignKey('user_photos.photo_id'), nullable=False)
    post_text = db.Column(db.String, nullable=True)
    post_date = db.Column(db.DateTime)

    user_fk = db.relationship(User)
    photo_fk = db.relationship(PostPhoto)


class PostComment(db.Model):
    __tablename__ = 'post_comments'
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('user_post.post_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    comment_text = db.Column(db.String, nullable=True)
    comment_date = db.Column(db.DateTime)

    user_fk = db.relationship(User)
    post_fk = db.relationship(Post)


class HashTag(db.Model):
    __tablename__ = 'hashtags'
    hashtag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('user_post.post_id'), nullable=False)
    hashtag_name = db.Column(db.String, nullable=False)

    post_fk = db.relationship(Post)
