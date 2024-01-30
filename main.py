from PyQt5.QtWidgets import QApplication
from GUI.MainPage import MainPage
from GUI.PageController import PageController
import sys

QApp = QApplication(sys.argv)
application = MainPage()
controller = PageController(application.homePage,application.recipePage,application)
sys.exit(QApp.exec_())