from PyQt5.QtWidgets import QApplication, QWidget
import sys

def ui_startup():
    app = QApplication(sys.argv)
    app.setApplicationName("GitGud")

    window = QWidget()
    window.show()
    window.setStyleSheet("background-color: #262626;")

    app.exec()
    