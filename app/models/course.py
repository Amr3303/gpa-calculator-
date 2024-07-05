class Course():
    def __init__(self, code, title, credit_hours, degree, semester_num, grade, gpa, type, prerequists = None):
        self. code = code
        self.title = title
        self.credit_hours = credit_hours
        self.degree = degree
        self.prerequists = prerequists
        self.semester_num = semester_num
        self.grade = grade
        self.gpa = gpa
        self.type = type