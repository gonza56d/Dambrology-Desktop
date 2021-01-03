from enum import Enum

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QFont
from PyQt5.QtWidgets import QLineEdit, QCalendarWidget

from business.exceptions import DambrologyGuiException


class Validators(Enum):
    TEXT = 'TEXT'
    NUMBER = 'NUMBER'

    @classmethod
    def regex_type(cls, validator):
        if validator is cls.TEXT:
            return '[a-z-A-Z\\s]+'
        elif validator is cls.NUMBER:
            return '[0-9]+'


class DLineEdit(QLineEdit):

    def __init__(self, parent, x_pos, y_pos, validator=None):
        super().__init__(parent=parent)
        self.move(x_pos, y_pos)
        self.setFont(QFont('Ubuntu', 16))
        if validator:
            if not isinstance(validator, Validators):
                raise DambrologyGuiException(
                    "Expected parameter 'validator' as <enum 'resources.components.inputs.Validators'>")
            regex = QRegExp(Validators.regex_type(validator))
            validator = QRegExpValidator(regex)
            self.setValidator(validator)


class DCalendar(QCalendarWidget):

    def __init__(self, parent, x_pos, y_pos):
        super().__init__(parent=parent)
        self.move(x_pos, y_pos)
        self.setFont(QFont('Ubuntu', 16))
