from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit, QItemDelegate, QHeaderView
from PyQt5.QtCore import Qt, QRegularExpression
from PyQt5.QtGui import QKeyEvent, QRegularExpressionValidator, QIntValidator

from ..viewmodels.settings_vm import SettingsViewModel

class Settings(QMainWindow):
    def __init__(self, mw, parent=None):
        super(Settings, self).__init__(parent)
        self.main_window = mw
        self.main_window.btn_delete_all_data.clicked.connect(self.on_delete_button)
        self.viewmodel = SettingsViewModel()
        
        
    def on_delete_button(self):
        print("delete button clicked")
        if self.show_warning_message():
            if self.viewmodel.delete_all_data():
                self.show_success_message()
    
    def show_warning_message(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Ayoo chill bro")
        msgBox.setInformativeText(f"Are you sure about that? you will delete everything.")
        msgBox.setWindowTitle("Warning")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msgBox.exec() == QMessageBox.Ok
    
    def show_success_message(self):
        msgBoxDone = QMessageBox()
        msgBoxDone.setIcon(QMessageBox.Information)
        msgBoxDone.setText("Deleted")
        msgBoxDone.setInformativeText("All your data have been deleted ):")
        msgBoxDone.setWindowTitle("Confirmation")
        msgBoxDone.exec()