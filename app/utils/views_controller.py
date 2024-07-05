import sys
import os
import mysql.connector

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from ..views.initial_interface import InitialInterfaceForm
from app.views.main_interface import MainWindowForm
from PyQt5.QtWidgets import QApplication


class EmptyFieldError(Exception):
    pass

class Controller():
    def __init__(self, host="localhost", user= "root", passwrod = "287491", database="student_info"):
        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = passwrod,
            database = database
        )
        self.handle_views()
    
    def get_student_info(self):
        mycursor = self.connection.cursor()
        try:
            mycursor.execute("""
                SELECT first_name, last_name, code, email, level
                FROM student
            """)
            result = mycursor.fetchone()
            if result is None or None in result:
                raise EmptyFieldError("One or more fields are empty.")
            else:
                return {
                    'first_name': result[0],
                    'last_name': result[1],
                    'code': result[2],
                    'email': result[3],
                    'level': result[4]
                }
        except EmptyFieldError as e:
            print(f"First Time using the app: {e}")
            return None
        except Exception as ee:
            print(f"An error occurred: {ee}")
            return None
    
    def handle_views(self):
        app = QApplication(sys.argv)
        try:
            data = self.get_student_info()
            if data == None:
                form = InitialInterfaceForm()
                form.show()
                sys.exit(app.exec_())
            else:
                form = MainWindowForm()
                form.show()
                sys.exit(app.exec_())
        except:
            print("something went wrong!")
            

