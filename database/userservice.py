from database.models import User, Password, db


def register_user_db(**user_data):
    new_user = User(**user_data)

    db.session.add(new_user)
    db.session.commit()


def check_user_db(email):
    checker = User.query.filter_by(email=email).first()

    if checker:
        return checker.user_id
    return False


def check_user_password_db(email, password):
    user_id_db = check_user_db(email=email)

    checker = Password.query.filter_by(user_id=user_id_db, password=password).first()
    if checker:
        return True
    return False


def get_all_users_db():
    users = User.query.all()

    return users


def get_exact_user_db(user_id):
    exact_user = User.query.filter_by(user_id=user_id).first()

    return exact_user


def delete_user_db(user_id):
    user = User.query.filter_by(user_id=user_id).first()

    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False
