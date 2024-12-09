import datetime
class RegisterDTO:
    def __init__(self, firstname: str, lastname: str, birthdate: datetime.date, email: str, country: str, phonenumber: str, password: str):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.email = email
        self.country = country
        self.phonenumber = phonenumber
        self.password = password
