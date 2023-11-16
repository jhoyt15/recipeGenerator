from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from GUI.HomePage import HomePage
from GUI.RecipePage import RecipePage
class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage,self).__init__()
        self.setWindowTitle("Recipe Generator")
        self.setWindowIcon(QIcon("GUI/Images/HomePageIcon.jpg"))
        self.createUI()
        with open("GUI/Styles/MainPage.css","r") as file:
            self.setStyleSheet(file.read())

    def createUI(self) -> None:
        self.navigationTab = QTabWidget()
        self.navigationTab.setObjectName("navTab")
        self.navigationTab.setTabPosition(QtWidgets.QTabWidget.South)

        self.homePage = HomePage()
        self.recipePage = RecipePage()

        homePageIcon = QIcon("GUI/Images/homePageIcon.png")

        recipePageIcon = QIcon("GUI/Images/recipePageIcon.png")

        self.navigationTab.addTab(self.homePage,homePageIcon,"Home")

        self.navigationTab.addTab(self.recipePage,recipePageIcon,"Recipes")\
        
        self.setCentralWidget(self.navigationTab)
        #self.navigationTab.setStyleSheet("background-color: rgb(40,40,40); border: none;")

        self.show()