from PyQt5.QtCore import QObject, pyqtSignal
from app.DAOs.show_courses_dao import ShowCoursesDAO
from app.DAOs.database import DataBaseDAO


class SettingsViewModel(QObject):
    courses_fetched = pyqtSignal(list)
    
    def __init__(self):
        super().__init__()
        self.dao = ShowCoursesDAO()
        self.database = DataBaseDAO()
        
    def delete_all_data(self):
        self.database.delete_all_data()
        self.database.update_student_info()
        return True