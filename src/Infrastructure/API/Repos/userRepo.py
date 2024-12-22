
from Infrastructure.API.DbConfig import SessionLocal
from Infrastructure.Domain.Entities.User import User


class UserRepository:
    def __init__(self):
        self.session = SessionLocal()

    def get_all_users(self):
        users = self.session.query(User).all()
        return users

    def get_user_by_id(self, user_id):
        user = self.session.query(User).filter(User.id == user_id).first()
        return user

    def create_user(self, username, email):
        new_user = User(username=username, email=email)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update_user(self, user_id, username=None, email=None):
        user = self.session.query(User).filter(User.id == user_id).first()
        if not user:
            return None

        if username:
            user.username = username
        if email:
            user.email = email

        self.session.commit()
        return user

# In professional work, data deletion is typically not allowed. Instead, we can implement a property called isDeleted. For example, if a user wants to delete a post from their profile, we can set isDeleted=True instead of removing the record from the database. As a result, our get_all query should be updated to something like get_all_active() or get_all_where_isDeletedFale() etc... , applying a condition to filter only the active records where isDeleted=False. Its called "Soft Deletion".
# if you really want to delete some data you should add some auth funct and new repo which is called Remove_User (only Super Admin can Use).
    
    def delete_user(self, user_id):
        user = self.session.query(User).filter(User.id == user_id).first()
        if not user:
            return False

        self.session.delete(user)
        self.session.commit()
        return True