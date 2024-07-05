from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit, QItemDelegate, QFileDialog
from PyQt5.QtCore import Qt, QRegularExpression
from PyQt5.QtGui import QKeyEvent, QRegularExpressionValidator, QIntValidator

import csv

from ..viewmodels.show_courses_vm import ShowCoursesViewModel


class UppercaseLineEdit(QLineEdit):
    def keyPressEvent(self, event):
        if event.text().isalpha():
            event = QKeyEvent(
                event.type(), event.key(), event.modifiers(), event.text().upper()
            )
        super().keyPressEvent(event)


class IntegerValidatorDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        regexp = QRegularExpression("([0-9]+)?")
        validator = QRegularExpressionValidator(regexp)
        editor.setValidator(validator)
        return editor


class ShowCourses(QMainWindow):
    def __init__(self, mw, parent=None):
        super(ShowCourses, self).__init__(parent)
        self.main_window = mw
        self.handle_table()
        self.handle_le()
        self.viewmodel = ShowCoursesViewModel()
        self.viewmodel.courses_fetched.connect(self.update_table_ui_with_courses)
        # self.load_courses()
        self.handle_search_button()
        self.handle_export_button()
    def get_constraints(self):
        code = self.main_window.le_code.text()
        title = self.main_window.le_title.text()
        grade = self.main_window.cb_grade.currentText()
        credit_hours = self.main_window.cb_credit_hours.currentText()
        semester_type = self.main_window.cb_semester_type_2.currentText()
        semester_number = self.main_window.le_semester_number_2.text()
        return code, title, grade, credit_hours, semester_type, semester_number
    
    def load_courses(self):
        code, title, grade, credit_hours, semester_type, semester_number = self.get_constraints()
        
        print(f"code: {code}\n",
            f"title: {title}\n",
            f"grade: {grade}\n",
            f"credit_hours: {credit_hours}\n",
            f"semester_type: {semester_type}\n",
            f"semester_number: {semester_number}\n")
        
        courses = self.viewmodel.get_courses(code, title, grade, credit_hours, semester_type, semester_number)  # Fetch the data
        print("courses: ", courses)
        return courses
    
    def update_table_ui_with_courses(self, courses):
        self.main_window.table_show_courses.clearContents()  # Clear the existing contents
        self.main_window.table_show_courses.setRowCount(0)  # Reset the row count
        
        if not courses:
            QMessageBox.information(self, "No Data", "No courses found matching the criteria.")
            return
        
        self.main_window.table_show_courses.setRowCount(len(courses))  # Set the number of rows
        
        for i, course in enumerate(courses):
            item_code = QTableWidgetItem(str(course[0]))  # code
            item_code.setFlags(item_code.flags() & ~Qt.ItemIsEditable)
            self.main_window.table_show_courses.setItem(i, 0, item_code)
            
            item_title = QTableWidgetItem(str(course[1]))  # title
            item_title.setFlags(item_title.flags() & ~Qt.ItemIsEditable)
            self.main_window.table_show_courses.setItem(i, 1, item_title)
            
            item_grade = QTableWidgetItem(str(course[4]))  # grade
            item_grade.setFlags(item_grade.flags() & ~Qt.ItemIsEditable)
            self.main_window.table_show_courses.setItem(i, 2, item_grade)
            
            item_gpa = QTableWidgetItem(str(course[5]))  # gpa
            item_gpa.setFlags(item_gpa.flags() & ~Qt.ItemIsEditable)
            self.main_window.table_show_courses.setItem(i, 3, item_gpa)
            
            item_degree = QTableWidgetItem(str(course[2]))  # degree
            item_degree.setFlags(item_degree.flags() & ~Qt.ItemIsEditable)
            self.main_window.table_show_courses.setItem(i, 4, item_degree)
            
            item_credit_hours = QTableWidgetItem(str(course[3]))  # credit hours
            item_credit_hours.setFlags(item_credit_hours.flags() & ~Qt.ItemIsEditable)
            self.main_window.table_show_courses.setItem(i, 5, item_credit_hours)
            
            item_semester_number = QTableWidgetItem(str(course[6]))  # semester number
            item_semester_number.setFlags(item_semester_number.flags() & ~Qt.ItemIsEditable)
            self.main_window.table_show_courses.setItem(i, 6, item_semester_number)
    
    def handle_table(self):
        
        # header = self.main_window.table_show_courses.horizontalHeader()
        # header.setSectionResizeMode(QHeaderView.Stretch)
        
        # self.main_window.table_show_courses.resizeColumnsToContents()
        # resize the width of table
        self.main_window.table_show_courses.setColumnWidth(0, 120)
        self.main_window.table_show_courses.setColumnWidth(1, 152)
        self.main_window.table_show_courses.setColumnWidth(2, 100)
        self.main_window.table_show_courses.setColumnWidth(3, 100)
        self.main_window.table_show_courses.setColumnWidth(4, 100)
        self.main_window.table_show_courses.setColumnWidth(5, 200)
        self.main_window.table_show_courses.setColumnWidth(6, 200)
        self.main_window.table_show_courses.setSortingEnabled(True)  # Enable sorting
    
    def handle_search_button(self):
        self.main_window.btn_search.clicked.connect(self.on_search_button)
    
    def on_search_button(self):
        courses = self.load_courses()
        self.update_table_ui_with_courses(courses)
    
    def handle_le(self):
        self.main_window.le_semester_number_2.setValidator(QIntValidator())
    
    def handle_export_button(self):
        self.main_window.btn_export.clicked.connect(self.export_to_csv)
    
    def export_to_csv(self):
        # Open a file dialog to select the save location
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_name:
            # Get table data
            row_count = self.main_window.table_show_courses.rowCount()
            column_count = self.main_window.table_show_courses.columnCount()
            headers = [self.main_window.table_show_courses.horizontalHeaderItem(i).text() for i in range(column_count)]
            
            # Write data to CSV
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                for row in range(row_count):
                    row_data = []
                    for column in range(column_count):
                        item = self.main_window.table_show_courses.item(row, column)
                        row_data.append(item.text() if item else "")
                    writer.writerow(row_data)
            QMessageBox.information(self, "Export Successful", f"Data exported successfully to {file_name}")