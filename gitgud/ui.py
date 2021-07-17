from PyQt5.QtWidgets import QApplication, QWidget
import sys

def ui_startup():
    app = QApplication(sys.argv)

    window = QWidget()
    window.show()

    app.exec()