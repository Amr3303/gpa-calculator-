from PyQt5.QtWidgets import QApplication
from app.utils.views_controller import Controller
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Controller()
    form.show()
    sys.exit(app.exec_())
