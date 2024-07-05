import mysql.connector
from app.models.student import Student

class InitialInterfaceDao:
    def __init__(self, host="localhost", user="root", password="287491", database="student_info"):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def insert_student_data(self, student):
        cursor = self.connection.cursor()
        sql = "INSERT INTO Student (first_name, last_name, email, level, code) VALUES (%s, %s, %s, %s, %s)"
        val = (student.first_name, student.last_name, student.email, student.level, student.code)

        try:
            cursor.execute(sql, val)
            self.connection.commit()
            print("data has been saved successfully")
            return True
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False

    def close(self):
        self.connection.close()
