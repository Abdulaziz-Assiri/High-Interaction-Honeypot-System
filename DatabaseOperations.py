import mysql.connector
from mysql.connector import errorcode
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import time
from PySide6.QtWidgets import QMessageBox
from DatabaseConnection import *
from RPC_Client import RPC_Client
import threading

class DatabaseOperations:
    def sign_up(email, password):
        conn, cursor = DatabaseConnection.connect_to_db()
        if conn is None:
            return
        try:
            cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
            conn.commit()
            return True
        except mysql.connector.errors.IntegrityError as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                QMessageBox.critical(None, "Error", f"Error: An account already exists for '{email}'.")
        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"{err}")
            
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def login(email, password):
        conn, cursor = DatabaseConnection.connect_to_db()
        if conn is None:
            return
        try:
            cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
            user = cursor.fetchone()
            if user:
                return True
            else:
                QMessageBox.warning(None, "Warning", "Invalid email or password.")
        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"{err}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def reset_password(email):
        conn, cursor = DatabaseConnection.connect_to_db()
        if conn is None:
            return
        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            
            if user:
                reset_code = random.randint(000000,999999)
                reset_code = str(reset_code).zfill(6)
                DatabaseOperations.send_email(email, reset_code)

                cursor.execute("UPDATE users SET OTP = %s WHERE email = %s", (reset_code, email))
                conn.commit()       
                remove_code_thread = threading.Thread(target=DatabaseOperations.delete_reset_code, args=(email,))
                remove_code_thread.start()
                return True, reset_code

            else:
                QMessageBox.critical(None, "Error", "Invalid email.")
        except mysql.connector.Error as err:
                QMessageBox.critical(None, "Error", f"{err}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    @staticmethod
    def delete_reset_code(email):
        conn, cursor = DatabaseConnection.connect_to_db()
        time.sleep(120)
        cursor.execute("UPDATE users SET OTP = NULL WHERE email = %s", (email,))
        conn.commit() 
        cursor.close()
        conn.close()
    
    @staticmethod
    def send_email(receiver_email, reset_code, smtp_server="smtp.gmail.com", smtp_port=587):
        sender_email = "your Google email"
        sender_password = "your password"
        subject = "Honeypot Reset Code"

        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            html_message = f"""
            <html>
                <body style="font-size: 16px;">
                    <p >Dear User,</p>
                    <p>You've recently requested to reset your password. To complete the process, please use the following code:</p>
                    <strong>{reset_code}</strong>
                    <p style="color: red">This code is valid for 2 minutes only. After that, you'll need to request a new code.</p>
                    <strong>If you did not request a password reset, please ignore this email.</strong>
                    <p>Thank you,</p>
                    <p>The Honeypot Team</p>
                </body>
            </html>
            """
            msg.attach(MIMEText(html_message, 'html'))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)

        except Exception as e:
            QMessageBox.critical(None, "Error", f"{e}")
        
    def check_code(fields_content, reset_code):
        if fields_content == reset_code:
            return True
        else:
            QMessageBox.critical(None, "Error", "Error: Not correct code")
    
    def set_new_password(email, new_password):
        conn, cursor = DatabaseConnection.connect_to_db()
        cursor.execute("UPDATE users SET password = %s WHERE email = %s", (new_password, email))
        conn.commit()
        cursor.close()
        conn.close()

    

