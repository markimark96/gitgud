from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QMenu, QMenuBar, QPushButton, QStatusBar, QTabBar, QTabWidget, QToolBar, QToolButton, QVBoxLayout, QWidget, QMainWindow


class GitGudUi(QMainWindow):
    def __init__(self):
       super().__init__()
       self.setStyleSheet("background-color: #262626;")
       self.showMaximized()
       self._addMenuBar()
       self._addToolBar()
       self._addTabs()


    def _addMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setStyleSheet("background-color: #737373;")
        fileMenu = self.menuBar.addMenu('&File')
        editMenu = self.menuBar.addMenu('&Edit')
        helpMenu = self.menuBar.addMenu('&Help')
        openAction = fileMenu.addAction("Open")

    def _addToolBar(self):
        self.toolBar = self.addToolBar("toolBar")
        self.toolBar.setStyleSheet(
            "background-color: #052f4d;"+
            "color: white;"
            )
        self.toolBar.setMovable(False)
        refreshButton = self._createToolButton(self.toolBar,"gitgud/assets/refresh.png","Refresh")
        pushButton = self._createToolButton(self.toolBar,"gitgud/assets/push.png","Push")
        pullButton = self._createToolButton(self.toolBar,"gitgud/assets/pull.png","Pull")
        stashButton = self._createToolButton(self.toolBar,"gitgud/assets/stash.png","Stash")
        popButton = self._createToolButton(self.toolBar,"gitgud/assets/pop.png","Pop")
        """        
        pullMenu = QMenu("Kappa")
        pullMenu.addAction("Fetch")
        pullButton.setMenu(pullMenu)
        pullMenu
        pullButton.setPopupMode(QToolButton.InstantPopup)
        """



    def _createToolButton(self,toolBar,icon,buttonText):
        button = QToolButton(self)
        button.setIcon(QIcon(icon))
        button.setText(buttonText)
        button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        toolBar.addWidget(button)
        return button

    def _addTabs(self):
        self.tabs = QTabWidget(self)
        self.tab0 = QWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tabs.addTab(self.tab0,QIcon("gitgud/assets/add.png"),"")
        self.tabs.addTab(self.tab1,"Tab1")
        self.tabs.addTab(self.tab2,"Tab2")
        self.setCentralWidget(self.tabs)
        