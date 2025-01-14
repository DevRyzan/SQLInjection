import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../')))
from Infrastructure.Domain.Models.DTOs.UserDTOs.LoginDTO import LoginDTO

#python3 -m unittest src/Infrastructure/Domain/Models/DTOs/UserDTOs/test_login_dto.py

class TestLoginDTO(unittest.TestCase):

    def test_login_dto_initialization(self):
        # tests whether the LoginDTO object has been created correctly
        email = "test@example.com"
        password = "securepassword"

        # create DTO object
        login_dto = LoginDTO(email=email, password=password)

        # check if values ​​are assigned correctly
        self.assertEqual(login_dto.email, email)
        self.assertEqual(login_dto.password, password)

    def test_empty_email(self):
        # tests creating a LoginDTO with a blank email
        email = ""
        password = "securepassword"

        with self.assertRaises(ValueError):
            LoginDTO(email=email, password=password)

    def test_empty_password(self):
        # tests creating a LoginDTO with a blank password
        email = "test@example.com"
        password = ""

        with self.assertRaises(ValueError):
            LoginDTO(email=email, password=password)

    def test_invalid_email_format(self):
        # tests creating a LoginDTO with an invalid email format
        email = "invalid-email-format"
        password = "securepassword"

        with self.assertRaises(ValueError):
            LoginDTO(email=email, password=password)


if __name__ == "__main__":
    unittest.main()
