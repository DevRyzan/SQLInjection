import unittest
import datetime
from src.Infrastructure.Domain.Models.DTOs.UserDTOs.RegisterDTO import RegisterDTO

#python3 -m unittest src/Infrastructure/Domain/Models/DTOs/UserDTOs/test_register_dto.py

class TestRegisterDTO(unittest.TestCase):

    def test_register_dto_initialization(self):
        # tests whether the RegisterDTO object is created correctly
        firstname = "Sadik Emre"
        lastname = "Ikiz"
        birthdate = datetime.date(2001, 1, 20)
        email = "sadikemre@example.com"
        country = "Turkey"
        phonenumber = "1234567890"
        password = "securepassword"

        # create DTO object
        register_dto = RegisterDTO(
            firstname=firstname,
            lastname=lastname,
            birthdate=birthdate,
            email=email,
            country=country,
            phonenumber=phonenumber,
            password=password,
        )

        # check if values ​​are assigned correctly
        self.assertEqual(register_dto.firstname, firstname)
        self.assertEqual(register_dto.lastname, lastname)
        self.assertEqual(register_dto.birthdate, birthdate)
        self.assertEqual(register_dto.email, email)
        self.assertEqual(register_dto.country, country)
        self.assertEqual(register_dto.phonenumber, phonenumber)
        self.assertEqual(register_dto.password, password)

    def test_empty_email(self):
        # tests creating RegisterDTO with a blank email
        firstname = "Sadik Emre"
        lastname = "Ikiz"
        birthdate = datetime.date(2001, 1, 20)
        email = ""  # empty mail
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
        # tests whether an error is thrown when a birth date is given with a future date
        firstname = "Sadik Emre"
        lastname = "Ikiz"
        birthdate = datetime.date(2030, 1, 1)  # invalid date (future)
        email = "sadikemre@example.com"
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
        # tests creating RegisterDTO with a blank password
        firstname = "Sadik Emre"
        lastname = "Ikiz"
        birthdate = datetime.date(1990, 5, 15)
        email = "sadikemre@example.com"
        country = "Turkey"
        phonenumber = "1234567890"
        password = ""  # empty password

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
