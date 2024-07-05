from PyQt5.QtCore import QObject, pyqtSignal
from app.DAOs.show_courses_dao import ShowCoursesDAO
from app.DAOs.database import DataBaseDAO

class ShowCoursesViewModel(QObject):
    courses_fetched = pyqtSignal(list)
    
    def __init__(self):
        super().__init__()
        self.dao = ShowCoursesDAO()
        
        
        
    def get_courses(self, code, title, grade, credit_hours, semester_type, semester_number):
        courses = self.dao.get_courses_from_db(code, title, grade, credit_hours, semester_type, semester_number)
        if courses:
            self.courses_fetched.emit(courses)
            return courses
    