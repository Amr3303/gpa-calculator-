import mysql.connector

class DataBaseDAO:
    def __init__(self, host="localhost", user="root", password="287491", database="student_info"):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    
    def update_student_info(self):
        cursor = self.connection.cursor()
        gpa = self.get_total_gpa()
        level = self.get_level()
        warnings = self.get_warnings()
        hours_passed = self.get_hours_passed()
        grade = self.get_total_grade()
        print("Trying to update student data")
        try:
            query = "UPDATE student SET warnings = %s, level = %s, total_gpa = %s, hours_passed = %s, total_grade = %s WHERE id = 1"
            values = (warnings, level, gpa, hours_passed, grade)
            print("Update values:", values)  # Debugging
            cursor.execute(query, values)
            self.connection.commit()  # Commit the transaction
            cursor.close()
            print("Student data has been updated")
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return 
    
    def get_warnings(self):
        warnings = 0
        cursor = self.connection.cursor()
        try:
            sql = "SELECT DISTINCT semester_no FROM course"
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            
            # Extract semester numbers from the results and save them in a list
            semester_numbers = [row[0] for row in results]
            semester_numbers.sort()
            for i in semester_numbers:
                semester_gpa = self.get_semester_gpa(i)
                if semester_gpa < 2:
                    warnings += 1
                elif semester_gpa >= 2:
                    warnings = 0
                    
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return 
        print("Semester numbers from database:", semester_numbers)
        return warnings
    
    def get_level(self):
        level = 0
        hours = self.get_hours_passed()
        if hours < 33:
            level = 1
        elif (hours >= 33) and (hours < 69):
            level = 2
        elif (hours >= 69) and (hours < 104):
            level = 3
        elif (hours >= 104):
            level = 4
        return level
    
    def get_total_gpa(self):
        cursor = self.connection.cursor()
        courses = []
        try:
            sql = "SELECT * FROM course"
            cursor.execute(sql)
            courses = cursor.fetchall()
            cursor.close()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return 
        print("courses from database", courses)
        gpa = 0.0
        numerator = 0.0
        denominator = 0.0
        if len(courses) != 0:
            # print("len > 0")
            for course in courses:
                numerator += float(course[3]) * float(course[5])
                denominator += float(course[3])
                # gpa += self.get_course_gpa(course[3], course[5])
            gpa = numerator / denominator
            print("gpa = ", gpa)
            return gpa
        
    def get_hours_passed(self, semester_no = None):
        cursor = self.connection.cursor()
        courses = []
        hours = 0
        if semester_no == None:
            try:
                query = "SELECT * FROM course WHERE gpa >= 2"
                cursor.execute(query)
                courses = cursor.fetchall()
                # print("courses gpa >= 2", courses)
                cursor.close()
                for course in courses:
                    hours += course[3]
                return hours
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
                return 
        else:
            try:
                query = "SELECT * FROM course WHERE semester_no <= %s AND gpa >= 2"
                cursor.execute(query, (semester_no,))
                courses = cursor.fetchall()
                cursor.close()
                for course in courses:
                    hours += course[3]
                return hours
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
                return 
            
    def get_total_grade(self):
        gpa = self.get_total_gpa()
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
        
    def get_course_gpa(self, credit_hours, gpa):
        return float((float(credit_hours) * float(gpa)) / float(credit_hours))
        
    def get_semester_gpa(self, semester_no):
        cursor = self.connection.cursor()
        courses = []
        try:
            sql = "SELECT * FROM course WHERE semester_no = %s"
            cursor.execute(sql, (semester_no,))
            courses = cursor.fetchall()
            cursor.close()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return 
        print("courses from database", courses)
        gpa = 0.0
        numerator = 0.0
        denominator = 0.0
        if len(courses) != 0:
            # print("len > 0")
            for course in courses:
                if course[3] > 0:
                    numerator += float(course[3]) * float(course[5])
                    denominator += float(course[3])
                # gpa += self.get_course_gpa(course[3], course[5])
            gpa = numerator / denominator
            # print("gpa = ", gpa)
            return gpa
        
    def get_total_gpa_till_semester_no(self, semester_no):
        cursor = self.connection.cursor()
        courses = []
        try:
            sql = "SELECT * FROM course WHERE semester_no <= %s"
            cursor.execute(sql, (semester_no,))
            courses = cursor.fetchall()
            cursor.close()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return 
        # print("courses from database", courses)
        gpa = 0.0
        numerator = 0.0
        denominator = 0.0
        if len(courses) != 0:
            # print("len > 0")
            for course in courses:
                if course[3] > 0:
                    numerator += float(course[3]) * float(course[5])
                    denominator += float(course[3])
                # gpa += self.get_course_gpa(course[3], course[5])
            gpa = numerator / denominator
            print("gpa = ", gpa)
            return gpa
    
    def delete_course(self):
        ...
    
    def delete_all_data(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM course;")
            cursor.execute("DELETE FROM semester;")
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            cursor.close()