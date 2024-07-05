from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from ..viewmodels.basic_informations_vm import BasicInformationsViewModel

class BasicInformations(QMainWindow):
    def __init__(self, mw, parent=None):
        super(BasicInformations, self).__init__(parent)
        self.main_window = mw
        self.initUI()
        self.viewmodel = BasicInformationsViewModel()
        self.viewmodel.data_fetched.connect(self.update_ui_with_data)  # Connect the signal to the slot
        self.load_student_data()
    
    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

    def load_student_data(self):
        self.viewmodel.get_student_data()  # Fetch the data

    def update_ui_with_data(self, student_data):
        # Update the UI with the fetched data
        self.main_window.label_8.setText(str(student_data[1]))  # Level
        self.main_window.label_6.setText(str(student_data[2]))  # Warnings
        self.main_window.label_2.setText(str(student_data[0]))  # GPA
        self.main_window.label_9.setText(str(student_data[3]))  # Total Grade
        self.main_window.label_4.setText(str(student_data[4]))  # Hours Passed

