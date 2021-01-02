import sys

from PyQt5.QtWidgets import QApplication

from resources.new_study_window import NewStudyWindow

app = QApplication(sys.argv)
study_window = NewStudyWindow(app)
