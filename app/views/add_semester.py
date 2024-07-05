from PyQt5.QtCore import QModelIndex, QEvent, Qt, QRegularExpression
from PyQt5.QtGui import QIntValidator, QRegularExpressionValidator, QKeyEvent
from PyQt5.QtWidgets import QItemDelegate, QLineEdit, QMainWindow, QMessageBox, QHeaderView
from ..viewmodels.add_semester_vm import AddSemesterViewModel


class UppercaseLineEdit(QLineEdit):
    def keyPressEvent(self, event):
        if event.text().isalpha():
            event = QKeyEvent(
                event.type(), event.key(), event.modifiers(), event.text().upper()
            )
        super().keyPressEvent(event)


class UppercaseDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = UppercaseLineEdit(parent)
        return editor


class CharacterValidatorDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        regexp = QRegularExpression("([a-z A-Z 0-9 ]+)?")
        validator = QRegularExpressionValidator(regexp)
        editor.setValidator(validator)
        return editor


class IntegerValidatorDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        regexp = QRegularExpression("([0-9]+)?")
        validator = QRegularExpressionValidator(regexp)
        editor.setValidator(validator)
        return editor


class AddSemester(QMainWindow):
    def __init__(self, mw, parent=None):
        super(AddSemester, self).__init__(parent)
        self.main_window = mw
        self.viewmodel = AddSemesterViewModel()
        self.viewmodel.courses_data_saved.connect(self.on_courses_data_saved)
        self.viewmodel.courses_data_error.connect(self.on_courses_data_error)
        self.viewmodel.courses_data_duplicate.connect(self.on_courses_data_duplicate)
        self.all_buttons()
        self.handle_le()
        self.handle_table_add_semester()

    def handle_btn_save(self):
        if self.handel_missing_data():
            semester_no, semester_type, courses = self.extract_semester_data()
            print(courses)
            self.viewmodel.save_semester_data(semester_no, semester_type, courses)

    def handel_missing_data(self):
        missing_data = []
        if self.main_window.le_semester_number.text() == "" or self.main_window.le_semester_number.text() == "Semester Number":
            missing_data.append(f"Semester Number")
        if self.main_window.cb_semester_type.currentText() is None:
            missing_data.append(f"Semester Type")

        missing = []
        there_is_course = False
        for row in range(self.main_window.table_add_semester.rowCount()):
            there_is_course = True
            for column in range(self.main_window.table_add_semester.columnCount()):
                item = self.main_window.table_add_semester.item(row, column)
                if item is None or item.text() == "":
                    missing.append((row, column))
        tabel = {
            0: "Code",
            1: "Title",
            2: "Credit Hours",
            3: "Degree"
        }
        if not there_is_course:
            msgBoxMissing = QMessageBox()
            msgBoxMissing.setIcon(QMessageBox.Warning)
            msgBoxMissing.setText("Missing Information")
            msgBoxMissing.setInformativeText("There are no courses to be added")
            msgBoxMissing.setWindowTitle("Warning")
            msgBoxMissing.exec()
        for i, j in missing:
            if j in [0, 1, 2, 3]:
                missing_data.append(f"Row {i + 1}, Column: {tabel[j]}")
        if len(missing_data) != 0:
            msgBoxMissing = QMessageBox()
            msgBoxMissing.setIcon(QMessageBox.Warning)
            msgBoxMissing.setText("Missing Information")
            msgBoxMissing.setInformativeText("Please fill in the following fields:\n" + "\n".join(missing_data))
            msgBoxMissing.setWindowTitle("Warning")
            msgBoxMissing.exec()
        return (len(missing_data) == 0)

    def extract_semester_data(self):
        semester_no = self.main_window.le_semester_number.text()
        semester_type = self.main_window.cb_semester_type.currentText()
        table_courses = []
        for row in range(self.main_window.table_add_semester.rowCount()):
            row_data = []
            for column in range(self.main_window.table_add_semester.columnCount()):
                item = self.main_window.table_add_semester.item(row, column)
                row_data.append(item.text() if item else "")
            table_courses.append(row_data)
        return semester_no, semester_type, table_courses

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Delete:
                self.clear_selected_cells()
                return True
        return super().eventFilter(obj, event)

    def clear_selected_cells(self):
        for item in self.main_window.table_add_semester.selectedItems():
            item.setText("")

    def all_buttons(self):
        self.main_window.btn_add_table_row.clicked.connect(self.handle_btn_add_table_row)
        self.main_window.btn_delete_table_row.clicked.connect(self.handle_btn_delete_table_row)
        self.main_window.btn_add_instructor.clicked.connect(self.handle_btn_add_instructor)
        self.main_window.btn_save.clicked.connect(self.handle_btn_save)

    def handle_le(self):
        self.main_window.le_semester_number.setValidator(QIntValidator())

    def handle_btn_add_table_row(self):
        row_position = self.main_window.table_add_semester.rowCount()
        self.main_window.table_add_semester.insertRow(row_position)

    def handle_btn_delete_table_row(self):
        row_position = self.main_window.table_add_semester.rowCount()
        self.main_window.table_add_semester.removeRow(row_position-1)

    def handle_btn_add_instructor(self):
        col_position = self.main_window.table_add_semester.columnCount()
        self.main_window.table_add_semester.insertColumn(col_position)

    def handle_table_add_semester(self):
        header = self.main_window.table_add_semester.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        self.main_window.table_add_semester.resizeColumnsToContents()
        IntDelegate = IntegerValidatorDelegate(self.main_window.table_add_semester)
        CharactersDelegate = CharacterValidatorDelegate(self.main_window.table_add_semester)
        UpperDelegate = UppercaseDelegate(self.main_window.table_add_semester)
        self.main_window.table_add_semester.setItemDelegateForColumn(0, UpperDelegate)  # Set the delegate for the 1st column
        self.main_window.table_add_semester.setItemDelegateForColumn(1, CharactersDelegate) # Set the delegate for the 2nd column
        self.main_window.table_add_semester.setItemDelegateForColumn(2, IntDelegate)  # Set the delegate for the 3rd column
        self.main_window.table_add_semester.setItemDelegateForColumn(3, IntDelegate)  # Set the delegate for the 4th column
        self.main_window.table_add_semester.installEventFilter(self)

    def on_courses_data_saved(self):
        QMessageBox.information(None, "Success", "All courses have been saved successfully")

    def on_courses_data_error(self):
        QMessageBox.warning(None, "Error", "Error happened while saving courses data")

    def on_courses_data_duplicate(self, message):
        QMessageBox.warning(None, "Duplicate Entry", message)
