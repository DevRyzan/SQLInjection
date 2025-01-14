import unittest
import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../')))
from Infrastructure.Domain.Models.DTOs.UserDTOs.RegisterDTO import RegisterDTO

class TestRegisterDTO(unittest.TestCase):

    def test_register_dto_initialization(self):
        """Tests whether the RegisterDTO object is created correctly."""
        firstname = "John"
        lastname = "Doe"
        birthdate = datetime.date(1990, 5, 15)
        email = "johndoe@example.com"
        country = "USA"
        phonenumber = "1234567890"
        password = "securepassword"

        # Create DTO object
        register_dto = RegisterDTO(
            firstname=firstname,
            lastname=lastname,
            birthdate=birthdate,
            email=email,
            country=country,
            phonenumber=phonenumber,
            password=password,
        )

        # Check if values ​​are assigned correctly
        self.assertEqual(register_dto.firstname, firstname)
        self.assertEqual(register_dto.lastname, lastname)
        self.assertEqual(register_dto.birthdate, birthdate)
        self.assertEqual(register_dto.email, email)
        self.assertEqual(register_dto.country, country)
        self.assertEqual(register_dto.phonenumber, phonenumber)
        self.assertEqual(register_dto.password, password)

    def test_empty_email(self):
        """Tests creating RegisterDTO with a blank email."""
        firstname = "Sadik Emre"
        lastname = "Ikiz"
        birthdate = datetime.date(1990, 5, 15)
        email = ""  # Empty mail
        country = "Turkey"
        phonenumber = "1234567890"
        password = "securepassword"

        with self.assertRaises(ValueError):
            RegisterDTO(
                firstname=firstname,
                lastname=lastname,
                birthdate=birthdate,
                email=email,
                country=country,
                phonenumber=phonenumber,
                password=password,
            )

    def test_invalid_birthdate(self):
        """Tests whether an error is thrown when a birth date is given with a future date."""
        firstname = "Sadik Emre"
        lastname = "Ikiz"
        birthdate = datetime.date(2030, 1, 1)  # Invalid date (future)
        email = "johndoe@example.com"
        country = "Turkey"
        phonenumber = "1234567890"
        password = "securepassword"

        with self.assertRaises(ValueError):
            RegisterDTO(
                firstname=firstname,
                lastname=lastname,
                birthdate=birthdate,
                email=email,
                country=country,
                phonenumber=phonenumber,
                password=password,
            )

    def test_empty_password(self):
        """Tests creating RegisterDTO with a blank password."""
        firstname = "Sadik Emre"
        lastname = "Ikiz"
        birthdate = datetime.date(1990, 5, 15)
        email = "johndoe@example.com"
        country = "Turkey"
        phonenumber = "1234567890"
        password = ""  # Empty password

        with self.assertRaises(ValueError):
            RegisterDTO(
                firstname=firstname,
                lastname=lastname,
                birthdate=birthdate,
                email=email,
                country=country,
                phonenumber=phonenumber,
                password=password,
            )


if __name__ == "__main__":
    unittest.main()
