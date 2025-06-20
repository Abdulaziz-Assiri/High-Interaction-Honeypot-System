import mysql.connector
from PySide6.QtWidgets import QMessageBox

class DatabaseConnection:

    def connect_to_db():
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="honeypot_db"
            )
            cursor = conn.cursor()
            return conn, cursor
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Error connecting to the database: {err}")
            return None, None

