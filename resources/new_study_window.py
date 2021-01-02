import sys

from PyQt5.QtWidgets import QWidget, QLabel

from resources.components.inputs import GLineEdit, Validator
from resources.constants import constants, formatted_labels, labels


class NewStudyWindow(QWidget):

    def __init__(self, app):
        super().__init__()
        self.setWindowTitle(labels.DAMBROLOGY + ' | ' + labels.NEW_STUDY)
        screen = app.primaryScreen()
        size = screen.size()
        self.setGeometry(size.width() / 2 - constants.APP_WIDTH / 2, size.height() / 2 - constants.APP_HEIGHT / 2,
                         constants.APP_WIDTH, constants.APP_HEIGHT)
        self.setFixedSize(constants.APP_WIDTH, constants.APP_HEIGHT)
        self.set_labels()
        self.set_lines()
        self.show()
        sys.exit(app.exec_())

    def set_labels(self):
        init_height = 15
        lbl_names = QLabel(formatted_labels.NAMES, parent=self)
        lbl_names.move(60, init_height)
        lbl_last_names = QLabel(formatted_labels.LAST_NAMES, parent=self)
        lbl_last_names.move(60, init_height+100)
        lbl_birthday = QLabel(formatted_labels.BIRTHDAY, parent=self)
        lbl_birthday.move(60, init_height+200)

    def set_lines(self):
        init_height = 55
        line_names = GLineEdit(parent=self, x_pos=60, y_pos=init_height, validator=Validator.TEXT)
        line_last_names = GLineEdit(parent=self, x_pos=60, y_pos=init_height+100, validator=Validator.TEXT)
        line_birthdays = GLineEdit(parent=self, x_pos=60, y_pos=init_height+200)
