from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QMenuBar, QPushButton, QStatusBar, QToolBar, QToolButton, QWidget, QMainWindow


class GitGudUi(QMainWindow):
    def __init__(self):
       super().__init__()
       self.setStyleSheet("background-color: #262626;")
       self.showMaximized()
       self._addMenuBar()
       self._addToolBar()


    def _addMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setStyleSheet("background-color: #737373;")
        fileMenu = self.menuBar.addMenu('&File')
        editMenu = self.menuBar.addMenu('&Edit')
        helpMenu = self.menuBar.addMenu('&Help')
        openAction = fileMenu.addAction("Open")

    def _addToolBar(self):
        self.toolBar = self.addToolBar("Tool bar")