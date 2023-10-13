from models import db, User

class UserService:
    @staticmethod
    def create_user(username, password):
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return {'id': new_user.id, 'username': new_user.username}
