class LoginDTO:
    def __init__(self, email: str, password: str):
        if not email:
            raise ValueError("Email cannot be empty.")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        if not password:
            raise ValueError("Password cannot be empty.")
        self.email = email
        self.password = password