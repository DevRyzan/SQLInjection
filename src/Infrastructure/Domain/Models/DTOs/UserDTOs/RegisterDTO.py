import datetime
class RegisterDTO:
    def __init__(self, firstname: str, lastname: str, birthdate: datetime.date, email: str, country: str, phonenumber: str, password: str):
        if not email:
            raise ValueError("Email cannot be empty.")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        if not firstname or not lastname:
            raise ValueError("Firstname and lastname cannot be empty.")
        if birthdate > datetime.date.today():
            raise ValueError("Birthdate cannot be in the future.")
        if not password:
            raise ValueError("Password cannot be empty.")
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.email = email
        self.country = country
        self.phonenumber = phonenumber
        self.password = password