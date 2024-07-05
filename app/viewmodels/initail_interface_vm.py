# app/viewmodels/initial_setup_viewmodel.py
import re
from PyQt5.QtCore import QObject, pyqtSignal
from app.models.student import Student
from app.DAOs.initial_interface_dao import InitialInterfaceDao

class InitialInterfaceViewModel(QObject):
    data_saved = pyqtSignal(bool)
    error_occurred = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.dao = InitialInterfaceDao()
        self.student = None

    def save_student_data(self, first_name, last_name, email, level, code):
        self.student = Student(first_name, last_name, email, level, code)
        result = self.dao.insert_student_data(self.student)
        
        if result == True:
            self.data_saved.emit(True)
        else:
            self.error_occurred.emit("An error occurred while saving your information to the database.")
    
    def validate_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def close(self):
        self.dao.close()
