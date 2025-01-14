import sqlite3

class BookingRepository:
    def __init__(self, db_name="sql_injection.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            payment_info_id INTEGER
        );
        """
        self.cursor.execute(query)
        self.connection.commit()

    def create_booking(self, start_date, end_date, user_id, payment_info_id=None):
        query = f"""INSERT INTO bookings (start_date, end_date, user_id, payment_info_id)
                    VALUES ('{start_date}', '{end_date}', '{user_id}', {payment_info_id})"""
        try:
            self.cursor.execute(query)
            self.connection.commit()
            id = self.cursor.lastrowid
            return {"id": id, "user_id": user_id, "start_date": start_date, "end_date": end_date}
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return None

    def get_booking(self, booking_id):
        query = f"SELECT * FROM bookings WHERE id = {booking_id}"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            print(f"Booking Info: {result}")
            return result
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return None