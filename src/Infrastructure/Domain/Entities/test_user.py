import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.Infrastructure.API.DbConfig import Base
from src.Infrastructure.Domain.Entities.User import User

#python3 -m unittest src.Infrastructure.Domain.Entities.test_user

class TestUser(unittest.TestCase):
    def setUp(self):
        """Creates a temporary database before each test."""
        self.engine = create_engine("sqlite:///:memory:")  # A temporary SQLite database in memory
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def tearDown(self):
        """Closes the database after each test."""
        self.session.close()
        self.engine.dispose()

    def test_user_creation(self):
        """Tests whether a User object can be created and saved correctly."""
        user = User(
            id=1,
            username="testuser",
            email="testuser@example.com",
            password="securepassword",
            isDeleted=False
        )
        self.session.add(user)
        self.session.commit()

        # Retrieve user from database and check
        retrieved_user = self.session.query(User).filter_by(username="testuser").first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, "testuser@example.com")
        self.assertFalse(retrieved_user.isDeleted)

    def test_user_unique_constraint(self):
        """Tests if an error occurs when trying to add two users with the same username."""
        user1 = User(
            id=1,
            username="duplicateuser",
            email="user1@example.com",
            password="password1"
        )
        user2 = User(
            id=2,
            username="duplicateuser",
            email="user2@example.com",
            password="password2"
        )
        self.session.add(user1)
        self.session.commit()

        with self.assertRaises(Exception):  # Unique constraint violation expected
            self.session.add(user2)
            self.session.commit()


if __name__ == '__main__':
    unittest.main()
