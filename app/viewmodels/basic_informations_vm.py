from PyQt5.QtCore import QObject, pyqtSignal
from app.DAOs.basic_informations_dao import BasicInformationsDAO
from app.DAOs.database import DataBaseDAO

class BasicInformationsViewModel(QObject):
    data_fetched = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.database = DataBaseDAO()
        self.dao = BasicInformationsDAO()
    
    def get_student_data(self):
        student_data = self.dao.get_student_data_from_db()
        if student_data:
            self.data_fetched.emit(student_data)
            return student_data