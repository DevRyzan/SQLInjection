import datetime
class User:
    def __init__(self, id: int, firstname: str, lastname: str, birthdate: datetime.date, email: str, country: str, phonenumber: str, password: str):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.email = email
        self.country = country
        self.phonenumber = phonenumber
        self.password = password
