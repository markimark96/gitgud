from gitgud.ui import GitGudUi
from PyQt5.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("GitGud")
    demo = GitGudUi()
    demo.show()
    sys.exit(app.exec_())


