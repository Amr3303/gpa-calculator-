# utils/update_ui.py

def update_basic_informations_ui(main_window, viewmodel):
    """
    Update the student data in the main window using the provided viewmodel.
    
    Args:
        main_window (QMainWindow): The main window instance containing UI elements.
        viewmodel (BasicInformationsViewModel): The viewmodel instance to fetch updated data.
    """
    student_data = viewmodel.get_student_data()
    
    main_window.label_8.setText(str(student_data[1]))  # Level
    main_window.label_6.setText(str(student_data[2]))  # Warnings
    main_window.label_2.setText(str(student_data[0]))  # GPA
    main_window.label_9.setText(str(student_data[3]))  # Total Grade
    main_window.label_4.setText(str(student_data[4]))  # Hours Passed
