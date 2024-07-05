# app/views/initial_interface.py
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from app.viewmodels.initail_interface_vm import InitialInterfaceViewModel
from app.views.main_interface import MainWindowForm

import sys
import re

UiForm, _ = loadUiType(r'D:\python\Projects\GPA_Calculator\app\utils\ui_forms\initial_interface\initial_interface.ui')

class InitialInterfaceForm(QWidget, UiForm):
    def __init__(self, parent=None):
        super(InitialInterfaceForm, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        
        self.viewmodel = InitialInterfaceViewModel()
        self.viewmodel.data_saved.connect(self.on_data_saved)
        self.viewmodel.error_occurred.connect(self.show_error_message)
        
        self.btn_submit.clicked.connect(self.submit)
        self.press_enter()
        self.handle_le()
    
    def press_enter(self):
        self.le_first_name.returnPressed.connect(self.le_last_name.setFocus)
        self.le_last_name.returnPressed.connect(self.le_email.setFocus)
        self.le_email.returnPressed.connect(self.cb_level.setFocus)
        self.cb_level.activated.connect(self.le_code.setFocus)
        self.le_code.returnPressed.connect(self.btn_submit.click)
    
    def handle_le(self):
        self.le_code.setValidator(QIntValidator()) 
        email_validator = QRegExpValidator(QRegExp("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}"))
        self.le_email.setValidator(email_validator)
    
    def submit(self):
        first_name = self.le_first_name.text()
        last_name = self.le_last_name.text()
        email = self.le_email.text()
        level = self.cb_level.currentText()
        code = self.le_code.text()

        if self.handle_missing_values():
            return

        if not self.viewmodel.validate_email(email):
            self.show_invalid_email()
            return
        
        if self.show_confirmation_dialog(first_name, last_name, email, level, code):
            self.viewmodel.save_student_data(first_name, last_name, email, level, code) # making a student instance and save the data into db
        else:
            print("User canceled the submissoin.")
    
    def handle_missing_values(self):
        fields = {
            "First Name": self.le_first_name.text(),
            "Last Name": self.le_last_name.text(),
            "Email": self.le_email.text(),
            "Level": self.cb_level.currentText(),
            "Code": self.le_code.text()
            }
        missing_fields = [name for name, value in fields.items() if not value]
        if missing_fields:
            msgBoxMissing = QMessageBox()
            msgBoxMissing.setIcon(QMessageBox.Warning)
            msgBoxMissing.setText("Missing Information")
            msgBoxMissing.setInformativeText("Please fill in the following fields:\n" + "\n".join(missing_fields))
            msgBoxMissing.setWindowTitle("Warning")
            msgBoxMissing.exec()
            return True

    def show_confirmation_dialog(self, first_name, last_name, email, level, code):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Please confirm your information:")
        msgBox.setInformativeText(f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nLevel: {level}\nCode: {code}")
        msgBox.setWindowTitle("Confirmation")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msgBox.exec() == QMessageBox.Ok
    
    def on_data_saved(self):
        self.show_success_message()
        self.main_window = MainWindowForm()
        self.main_window.show()
        self.close()

    def show_success_message(self):
        msgBoxDone = QMessageBox()
        msgBoxDone.setIcon(QMessageBox.Information)
        msgBoxDone.setText("Success!")
        msgBoxDone.setInformativeText("Your information has been successfully saved to the database.")
        msgBoxDone.setWindowTitle("Confirmation")
        msgBoxDone.exec()
    
    def show_error_message(self, error_message):
        msgBoxError = QMessageBox()
        msgBoxError.setIcon(QMessageBox.Critical)
        msgBoxError.setText("Error!")
        msgBoxError.setInformativeText(error_message)
        msgBoxError.setWindowTitle("Error")
        msgBoxError.exec()
    
    def show_invalid_email(self):
        msgboxInvalidEmail = QMessageBox()
        msgboxInvalidEmail.setIcon(QMessageBox.Warning)
        msgboxInvalidEmail.setWindowTitle("Invalid.")
        msgboxInvalidEmail.setInformativeText("Invalid email address")
        msgboxInvalidEmail.setText("Invalid Email")
        msgboxInvalidEmail.exec()
