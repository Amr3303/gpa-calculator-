from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

from ..views.add_semester import AddSemester
from ..views.basic_informations import BasicInformations
from ..views.show_courses import ShowCourses
from ..views.settings import Settings

import sys
import re

UiForm, _ = loadUiType(r'D:\python\Projects\GPA_Calculator\app\utils\ui_forms\main_interface\main.ui')

class MainWindowForm(QMainWindow, UiForm):
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.handle_all_buttons()
        self.handle_tab_main()
        self.add_semseter = AddSemester(self)
        self.basic_informations = BasicInformations(self)
        self.show_courses = ShowCourses(self)
        self.settings = Settings(self)
        
        # Connect the data_updated signal to a slot
        self.add_semseter.viewmodel.data_updated.connect(self.refresh_basic_informations)
    
    def handle_all_buttons(self):
        self.btn_academic_informations.clicked.connect(self.open_academic_information_tap)
        self.btn_add_semester.clicked.connect(self.open_add_semester)
        self.btn_add_course.clicked.connect(self.open_add_course)
        self.btn_edit_informations.clicked.connect(self.open_edit_infromations)
        self.btn_settings.clicked.connect(self.open_settings)
    
    def open_academic_information_tap(self):
        self.tab_main.setCurrentIndex(0)
    
    def open_add_semester(self):
        self.tab_main.setCurrentIndex(1)
    
    def open_add_course(self):
        self.tab_main.setCurrentIndex(2)
    
    def open_edit_infromations(self):
        self.tab_main.setCurrentIndex(3)
    
    def open_settings(self):
        self.tab_main.setCurrentIndex(4)
        
    def handle_tab_main(self):
        # hide the bar of the main tab
        self.tab_main.tabBar().hide()
        
        # hide the bar of the sub tab in the academic informations
        self.tabWidget_2.tabBar().hide()
        
    def refresh_basic_informations(self):
        # Reinitialize the BasicInformations instance to refresh the UI
        self.basic_informations = BasicInformations(self)
