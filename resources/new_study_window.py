import sys

from PyQt5.QtWidgets import QWidget

from resources.components.buttons import DButton
from resources.components.inputs import DLineEdit, Validators, DCalendar
from resources.components.labels import DLabel
from resources.constants import app_constants
from resources.constants.labels import FormattedLabels, Labels


class NewStudyWindow(QWidget):

    lbl_names = None
    input_names = None
    lbl_last_names = None
    input_last_names = None
    lbl_birthday = None
    input_birthday = None
    btn_calculate = None

    def __init__(self, app):
        super().__init__()
        self.setWindowTitle(str(Labels.DAMBROLOGY) + ' | ' + str(Labels.NEW_STUDY))
        screen = app.primaryScreen()
        size = screen.size()
        self.setGeometry(size.width() / 2 - app_constants.APP_WIDTH / 2, size.height() / 2 - app_constants.APP_HEIGHT / 2,
                         app_constants.APP_WIDTH, app_constants.APP_HEIGHT)
        self.setFixedSize(app_constants.APP_WIDTH, app_constants.APP_HEIGHT)
        self.set_labels()
        self.set_inputs()
        self.set_buttons()
        self.show()
        sys.exit(app.exec_())

    def set_labels(self):
        init_height = app_constants.TOP_MARGIN
        self.lbl_names = DLabel(value=FormattedLabels.NAMES, parent=self, x_pos=app_constants.LEFT_MARGIN,
                                y_pos=init_height)
        self.lbl_last_names = DLabel(value=FormattedLabels.LAST_NAMES, parent=self, x_pos=app_constants.LEFT_MARGIN,
                                     y_pos=init_height+100)
        self.lbl_birthday = DLabel(value=FormattedLabels.BIRTHDAY, parent=self, x_pos=app_constants.LEFT_MARGIN,
                                   y_pos=init_height+200)

    def set_inputs(self):
        init_height = app_constants.TOP_MARGIN + 40
        self.input_names = DLineEdit(parent=self, x_pos=app_constants.LEFT_MARGIN, y_pos=init_height,
                                     validator=Validators.TEXT)
        self.input_last_names = DLineEdit(parent=self, x_pos=app_constants.LEFT_MARGIN, y_pos=init_height + 100,
                                          validator=Validators.TEXT)
        self.input_birthday = DCalendar(self, x_pos=app_constants.LEFT_MARGIN, y_pos=init_height + 200)

    def set_buttons(self):
        self.btn_calculate = DButton(parent=self, text=Labels.CALCULATE, x_pos=app_constants.APP_WIDTH / 2 - 35,
                                     y_pos=app_constants.APP_HEIGHT - 70)
