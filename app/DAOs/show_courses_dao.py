import mysql.connector
from app.models.course import Course

class ShowCoursesDAO:
    def __init__(self, host="localhost", user="root", password="287491", database="student_info"):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
    def get_courses_from_db(self, code=None, title=None, grade=None, credit_hours=None, semester_type=None, semester_number=None):
        cursor = self.connection.cursor()
        try:
            query = """
            SELECT c.* 
            FROM course c
            JOIN semester s ON c.semester_no = s.semester_no
            WHERE 1=1
            """
            constraints = []
            
            if code:
                query += " AND c.code LIKE %s"
                constraints.append(f"%{code}%")
            if title:
                query += " AND c.title LIKE %s"
                constraints.append(f"%{title}%")
            if grade != "-":
                query += " AND c.grade = %s"
                constraints.append(grade)
            if credit_hours != "-":
                query += " AND c.credit_hours = %s"
                constraints.append(credit_hours)
            if semester_type != "-":
                query += " AND s.type = %s"
                constraints.append(semester_type)
            if semester_number:
                query += " AND c.semester_no = %s"
                constraints.append(semester_number)
                
            cursor.execute(query, constraints)
            courses = cursor.fetchall()
            cursor.close()
            return courses
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return
