from Infrastructure.API.DbConfig import SessionLocal
from Infrastructure.Domain.Entities.User import User

#This class for Conext class. these repos will be move in our repos layer "add_user and get_all?users". I have held them for quick testing
class DbContext:
    def __init__(self):
        self.session = SessionLocal()

    def add_user(self, username, email):
        try:
            new_user = User(username=username, email=email)
            self.session.add(new_user)
            self.session.commit()
            print(f"✅ User Created: {username}")
        except Exception as e:
            print(f"❌ User Create Error {e}")
            self.session.rollback()
        finally:
            self.session.close()

    def get_all_users(self):
        try:
            users = self.session.query(User).all()
            for user in users:
                print(f"{user.id} | {user.username} | {user.email}")
            return users
        except Exception as e:
            print(f"❌ User list doesnt exists {e}")
        finally:
            self.session.close()