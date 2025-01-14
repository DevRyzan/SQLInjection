import unittest
from unittest.mock import MagicMock

#python3 -m unittest src.Infrastructure.Domain.Entities.test_user_with_mock

# Mock User class
User = MagicMock()
User.return_value.username = "testuser"
User.return_value.email = "test@example.com"
User.return_value.password = "securepassword"

# a class that simulates a mock repository
class MockUserRepository:
    def __init__(self):
        self.users = []

    def add(self, user):
        if any(u.username == user.username for u in self.users):
            raise ValueError("Username already exists.")
        self.users.append(user)

    def get_by_username(self, username):
        return next((u for u in self.users if u.username == username), None)

    def delete(self, user):
        self.users = [u for u in self.users if u != user]

class TestUserWithMock(unittest.TestCase):
    def setUp(self):
        # i create a mock repository
        self.mock_repo = MockUserRepository()

        # tests creating and adding users
    def test_user_creation(self):
        user = User(username="testuser", email="test@example.com", password="securepassword")
        self.mock_repo.add(user)
        retrieved_user = self.mock_repo.get_by_username("testuser")
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, "test@example.com")

    def test_user_unique_constraint(self):
        # if adding with the same username, an error is thrown
        user1 = User(username="duplicateuser", email="test1@example.com", password="pass1")
        user2 = User(username="duplicateuser", email="test2@example.com", password="pass2")
        self.mock_repo.add(user1)
        with self.assertRaises(ValueError):
            self.mock_repo.add(user2)

    def test_user_deletion(self):
        # tests deletion of user
        user = User(username="testuser", email="test@example.com", password="securepassword")
        self.mock_repo.add(user)
        self.mock_repo.delete(user)
        retrieved_user = self.mock_repo.get_by_username("testuser")
        self.assertIsNone(retrieved_user)

if __name__ == '__main__':
    unittest.main()


