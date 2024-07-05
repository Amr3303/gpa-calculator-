import mysql.connector
from app.models.course import Course

class AddSemesterDAO:
    def __init__(self, host="localhost", user="root", password="287491", database="student_info"):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def insert_courses_data(self, courses):
        cursor = self.connection.cursor()  
        for course in courses:
            
            # Check for duplicate in 'Code' with the same 'semester_number'
            query = "SELECT COUNT(*) FROM course WHERE Code = %s AND semester_no = %s"
            cursor.execute(query, (course.code, course.semester_num))
            result = cursor.fetchone()
            if result[0] > 0:
                return "DUPLICATE in Code"

            # Check for duplicate in 'title' with the same 'semester_number'
            query = "SELECT COUNT(*) FROM course WHERE title = %s AND semester_no = %s"
            cursor.execute(query, (course.title, course.semester_num))
            result = cursor.fetchone()
            if result[0] > 0:
                return "DUPLICATE in title"

            
            sql = "INSERT INTO course (Code, title, degree, credit_hours, grade, gpa, semester_no, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (course.code, course.title, course.degree, course.credit_hours, course.grade, course.gpa, course.semester_num, course.type)
            
            try:
                print("trying to insert")
                cursor.execute(sql, val)
                self.connection.commit()
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
                return 
        cursor.close()
        print("data has been saved successfully")
        return True

    def insert_or_update_semester_data(self, semester):
        cursor = self.connection.cursor()
        try:
            # Check if the semester already exists
            check_query = "SELECT COUNT(*) FROM semester WHERE semester_no = %s"
            cursor.execute(check_query, (semester.semester_no,))
            result = cursor.fetchone()

            if result[0] > 0:
                # If the semester exists, update the existing record
                print("semester already exists")
                update_query = """
                UPDATE semester
                SET semester_gpa = %s, total_gpa = %s, hours_passed_from_start = %s, semester_grade = %s
                WHERE semester_no = %s
                """
                values = (semester.semester_gpa, semester.total_gpa, semester.hours_passed_from_start, semester.semester_grade, semester.semester_no)
                cursor.execute(update_query, values)
            else:
                print("semester doesn't exists")
                # If the semester does not exist, insert a new record
                insert_query = """
                INSERT INTO semester(semester_no, type, semester_gpa, total_gpa, hours_passed_from_start, semester_grade)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                values = (semester.semester_no, semester.type, semester.semester_gpa, semester.total_gpa, semester.hours_passed_from_start, semester.semester_grade)
                cursor.execute(insert_query, values)
            
            self.connection.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return
        
        
        
    def close(self):
        self.connection.close()

    # def insert_semester_data(self, semester):
    #     cursor = self.connection.cursor()
    #     try:
    #         query = "INSERT INTO semester(semester_no, type, semester_gpa, total_gpa, hours_passed_from_start, semester_grade) VALUES (%s, %s, %s, %s, %s, %s)"
    #         values = (semester.semester_no, semester.type, semester.semester_gpa, semester.total_gpa, semester.hours_passed_from_start, semester.semester_grade)
    #         cursor.execute(query, values)
    #         self.connection.commit()
            
    #     except mysql.connector.Error as err:
    #         print("Something went wrong: {}".format(err))
    #         return 
        
        
        