# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python\Projects\GPA_Calculator\app\utils\ui_forms\main_interface\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1223, 796)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 221, 751))
        self.widget.setObjectName("widget")
        self.btn_academic_informations = QtWidgets.QPushButton(self.widget)
        self.btn_academic_informations.setGeometry(QtCore.QRect(10, 30, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_academic_informations.setFont(font)
        self.btn_academic_informations.setObjectName("btn_academic_informations")
        self.btn_add_semester = QtWidgets.QPushButton(self.widget)
        self.btn_add_semester.setGeometry(QtCore.QRect(10, 100, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_add_semester.setFont(font)
        self.btn_add_semester.setObjectName("btn_add_semester")
        self.btn_edit_informations = QtWidgets.QPushButton(self.widget)
        self.btn_edit_informations.setGeometry(QtCore.QRect(10, 250, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_edit_informations.setFont(font)
        self.btn_edit_informations.setObjectName("btn_edit_informations")
        self.btn_add_course = QtWidgets.QPushButton(self.widget)
        self.btn_add_course.setGeometry(QtCore.QRect(10, 180, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_add_course.setFont(font)
        self.btn_add_course.setObjectName("btn_add_course")
        self.btn_settings = QtWidgets.QPushButton(self.widget)
        self.btn_settings.setGeometry(QtCore.QRect(10, 670, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_settings.setFont(font)
        self.btn_settings.setObjectName("btn_settings")
        self.tab_main = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_main.setGeometry(QtCore.QRect(220, 10, 1001, 751))
        self.tab_main.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_main.setObjectName("tab_main")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 991, 711))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_information = QtWidgets.QWidget()
        self.tab_information.setObjectName("tab_information")
        self.label = QtWidgets.QLabel(self.tab_information)
        self.label.setGeometry(QtCore.QRect(10, 50, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_information)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_information)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_information)
        self.label_4.setGeometry(QtCore.QRect(230, 270, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_information)
        self.label_5.setGeometry(QtCore.QRect(10, 490, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_information)
        self.label_6.setGeometry(QtCore.QRect(230, 490, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_information)
        self.label_7.setGeometry(QtCore.QRect(10, 380, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_information)
        self.label_8.setGeometry(QtCore.QRect(230, 380, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_information)
        self.label_9.setGeometry(QtCore.QRect(230, 160, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_information)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.tabWidget_2.addTab(self.tab_information, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget.setGeometry(QtCore.QRect(0, 135, 981, 531))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.comboBox = QtWidgets.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(620, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_2.setGeometry(QtCore.QRect(390, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(540, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(270, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(10, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 161, 36))
        self.lineEdit.setObjectName("lineEdit")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(10, 80, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 30, 161, 36))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(260, 30, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 80, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_main.addTab(self.tab, "")
        self.tab_semester = QtWidgets.QWidget()
        self.tab_semester.setObjectName("tab_semester")
        self.table_add_semester = QtWidgets.QTableWidget(self.tab_semester)
        self.table_add_semester.setGeometry(QtCore.QRect(10, 210, 981, 451))
        self.table_add_semester.setObjectName("table_add_semester")
        self.table_add_semester.setColumnCount(6)
        self.table_add_semester.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_semester.setHorizontalHeaderItem(5, item)
        self.table_add_semester.horizontalHeader().setDefaultSectionSize(160)
        self.table_add_semester.verticalHeader().setDefaultSectionSize(58)
        self.btn_save = QtWidgets.QPushButton(self.tab_semester)
        self.btn_save.setGeometry(QtCore.QRect(368, 667, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.btn_add_table_row = QtWidgets.QPushButton(self.tab_semester)
        self.btn_add_table_row.setGeometry(QtCore.QRect(580, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_add_table_row.setFont(font)
        self.btn_add_table_row.setObjectName("btn_add_table_row")
        self.btn_delete_table_row = QtWidgets.QPushButton(self.tab_semester)
        self.btn_delete_table_row.setGeometry(QtCore.QRect(720, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_delete_table_row.setFont(font)
        self.btn_delete_table_row.setObjectName("btn_delete_table_row")
        self.le_semester_number = QtWidgets.QLineEdit(self.tab_semester)
        self.le_semester_number.setGeometry(QtCore.QRect(5, 71, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.le_semester_number.setFont(font)
        self.le_semester_number.setObjectName("le_semester_number")
        self.btn_add_instructor = QtWidgets.QPushButton(self.tab_semester)
        self.btn_add_instructor.setGeometry(QtCore.QRect(860, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_add_instructor.setFont(font)
        self.btn_add_instructor.setObjectName("btn_add_instructor")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_semester)
        self.comboBox_4.setGeometry(QtCore.QRect(575, 71, 106, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_19 = QtWidgets.QLabel(self.tab_semester)
        self.label_19.setGeometry(QtCore.QRect(390, 70, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.tab_main.addTab(self.tab_semester, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(210, 180, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.tab_main.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(200, 180, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.tab_main.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_18 = QtWidgets.QLabel(self.tab_5)
        self.label_18.setGeometry(QtCore.QRect(240, 190, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.tab_main.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_main.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_academic_informations.setText(_translate("MainWindow", "Academic Informations"))
        self.btn_add_semester.setText(_translate("MainWindow", "Add Semester"))
        self.btn_edit_informations.setText(_translate("MainWindow", "Edit Infomations"))
        self.btn_add_course.setText(_translate("MainWindow", "Add Coursse"))
        self.btn_settings.setText(_translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "GPA"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "Hours Passed"))
        self.label_4.setText(_translate("MainWindow", "49"))
        self.label_5.setText(_translate("MainWindow", "Warnings"))
        self.label_6.setText(_translate("MainWindow", "2"))
        self.label_7.setText(_translate("MainWindow", "Level"))
        self.label_8.setText(_translate("MainWindow", "2"))
        self.label_9.setText(_translate("MainWindow", "2"))
        self.label_10.setText(_translate("MainWindow", "Grade"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_information), _translate("MainWindow", "Basic Informations"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Course Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Grade"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "GPA"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Degree"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Credit Hours"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Semester"))
        self.comboBox.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox.setItemText(1, _translate("MainWindow", "A-"))
        self.comboBox.setItemText(2, _translate("MainWindow", "B+"))
        self.comboBox.setItemText(3, _translate("MainWindow", "B"))
        self.comboBox.setItemText(4, _translate("MainWindow", "C+"))
        self.comboBox.setItemText(5, _translate("MainWindow", "C"))
        self.comboBox.setItemText(6, _translate("MainWindow", "D"))
        self.comboBox.setItemText(7, _translate("MainWindow", "F"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Abs"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "A-"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "B+"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "B"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "C+"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "C"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "D"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "F"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Abs"))
        self.label_11.setText(_translate("MainWindow", "Grade"))
        self.label_12.setText(_translate("MainWindow", "Semester"))
        self.label_13.setText(_translate("MainWindow", "Code"))
        self.label_14.setText(_translate("MainWindow", "Credit Hours"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "A-"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "B+"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "B"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "C+"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "C"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "D"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "F"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "Abs"))
        self.label_15.setText(_translate("MainWindow", "Title"))
        self.pushButton_6.setText(_translate("MainWindow", "Search"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Courses"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        item = self.table_add_semester.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table_add_semester.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.table_add_semester.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.table_add_semester.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.table_add_semester.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.table_add_semester.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.table_add_semester.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Code"))
        item = self.table_add_semester.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.table_add_semester.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Credit Hours"))
        item = self.table_add_semester.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Degree"))
        item = self.table_add_semester.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Instructor"))
        item = self.table_add_semester.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Prerequisites"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.btn_add_table_row.setText(_translate("MainWindow", "Add Row"))
        self.btn_delete_table_row.setText(_translate("MainWindow", "Delete Row"))
        self.le_semester_number.setPlaceholderText(_translate("MainWindow", "Semester Number"))
        self.btn_add_instructor.setText(_translate("MainWindow", "Add Instructor"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Spring"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Fall"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Summer"))
        self.label_19.setText(_translate("MainWindow", "Semester Type"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_semester), _translate("MainWindow", "Tab 2"))
        self.label_16.setText(_translate("MainWindow", "Add Course"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.label_17.setText(_translate("MainWindow", "Edit Informations"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_2), _translate("MainWindow", "Page"))
        self.label_18.setText(_translate("MainWindow", "Settings"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_5), _translate("MainWindow", "Page"))
