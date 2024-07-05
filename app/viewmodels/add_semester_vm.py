from PyQt5.QtCore import QObject, pyqtSignal
from app.models.course import Course
from app.models.semester import Semester
from ..models.instructor import Instructor
from app.DAOs.add_semester_dao import AddSemesterDAO
from app.DAOs.database import DataBaseDAO
from app.viewmodels.basic_informations_vm import BasicInformationsViewModel

class AddSemesterViewModel(QObject):
    courses_data_saved = pyqtSignal(bool)
    courses_data_error = pyqtSignal(str)
    courses_data_duplicate = pyqtSignal(str)
    error_occurred = pyqtSignal(str)
    data_updated = pyqtSignal()  # New signal for data update

    def __init__(self):
        super().__init__()
        self.course = None
        self.semester = None
        self.database = DataBaseDAO()
        self.dao = AddSemesterDAO()
        self.basic_informations_vm = BasicInformationsViewModel()
    
    def get_gpa_and_grade(self, course):
        gpa = 0.0
        grade = None
        ch = course[2]
        degree = course[3]
        print(ch)
        percentage = 0.0
        if ch == "0":
            print("yesssssssssssssssssssssssssssss")
            percentage = float((int(degree) / 50) * 100)
            if percentage >= 60:
                grade = "P"
            else:
                grade = "F"
            gpa = 0.0
        else:
            percentage = float((int(degree) / (int(ch) * 50)) * 100)
            if percentage >= 90 :
                gpa = 4.00
                grade = "A"
            elif (percentage < 90) and (percentage >= 85):
                gpa = 3.67
                grade = "A-"
            elif (percentage < 85) and (percentage >= 80):
                gpa = 3.33
                grade = "B+"
            elif (percentage < 80) and (percentage >= 75):
                gpa = 3.00
                grade = "B"
            elif (percentage < 75) and (percentage >= 70):
                gpa = 2.67
                grade = "C+"
            elif (percentage < 70) and (percentage >= 65):
                gpa = 2.33
                grade = "C"
            elif (percentage < 65) and (percentage >= 60):
                gpa = 2.00
                grade = "D"
            elif (percentage < 60):
                gpa = 0.00
                grade = "F"
                
        return gpa, grade
    
    def get_semester_grade(self, gpa):
        grade = ""
        if gpa == 4.00 :
            grade = "A"
        elif (gpa < 4.00) and (gpa >= 3.67):
            grade = "A-"
        elif (gpa < 3.67) and (gpa >= 3.33):
            grade = "B+"
        elif (gpa < 3.33) and (gpa >= 3.00):
            grade = "B"
        elif (gpa < 3.00) and (gpa >= 2.67):
            grade = "C+"
        elif (gpa < 2.67) and (gpa >= 2.33):
            grade = "C"
        elif (gpa < 2.33) and (gpa >= 2.00):
            grade = "D"
        elif (gpa < 2.00):
            grade = "F"
            
        return grade
    
    def save_semester_data(self, semester_no, semester_type, courses):
        courses_instances = []
        _type = ""
        for c in courses:
            gpa, grade = self.get_gpa_and_grade(c)
            if int(c[2]) > 0:
                _type = "CH" # for credit hour
            else:
                _type = "UR" # for university requierments
            course = Course(c[0], c[1], c[2], c[3], semester_no, grade, gpa, type= _type)
            courses_instances.append(course)
            
        # inserting courses data
        result = self.dao.insert_courses_data(courses_instances)
        if result == True:
            self.courses_data_saved.emit(True)
        elif result == "DUPLICATE in title":
            self.courses_data_duplicate.emit("Duplicated values in title")
            return
        elif result == "DUPLICATE in Code":
            self.courses_data_duplicate.emit("Duplicated values in Code")
            return
        else:
            self.courses_data_error.emit("Error happened while saving courses data")
            return
        
        # Re-establish the database connection to ensure the latest data is fetched
        self.database = DataBaseDAO()
        
        # inserting semester data
        semester_gpa = self.database.get_semester_gpa(semester_no)
        print("semester_gpa: ", semester_gpa) 
        total_gpa_till_semester_no = self.database.get_total_gpa_till_semester_no(semester_no)
        hours_passed = self.database.get_hours_passed(semester_no)
        semester_grade = self.get_semester_grade(semester_gpa)
        semester = Semester(semester_no, semester_type, semester_gpa, total_gpa_till_semester_no, hours_passed, semester_grade)
        self.dao.insert_or_update_semester_data(semester)
        
        # Re-establish the database connection to ensure the latest data is fetched
        self.database = DataBaseDAO()
        
        # updating the student data
        self.database.update_student_info()
        
        # updating the basic informaitons ui
        self.basic_informations_vm.get_student_data()
        
        # Emit the signal to indicate data update
        self.data_updated.emit()