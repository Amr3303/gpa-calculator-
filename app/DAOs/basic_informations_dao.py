import mysql.connector

class BasicInformationsDAO:
    def __init__(self, host="localhost", user="root", password="287491", database="student_info"):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    
    def get_student_data_from_db(self):
        cursor = self.connection.cursor()
        try:
            query = "SELECT total_gpa, level, warnings, total_grade, hours_passed FROM student WHERE id = 1"
            cursor.execute(query)
            student_data = cursor.fetchall()
            cursor.close()
            student_data = list(student_data[0])
            return student_data
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return 