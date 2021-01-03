from enum import Enum

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QFont
from PyQt5.QtWidgets import QLineEdit, QCalendarWidget, QWidget

from business.exceptions import DambrologyGuiException


class Validators(Enum):
    """Input regex validators."""

    TEXT = 'TEXT'
    NUMBER = 'NUMBER'

    @classmethod
    def regex_type(cls, validator):
        """Return regex according to validator."""
        if validator is cls.TEXT:
            return '[a-z-A-Z\\s]+'
        elif validator is cls.NUMBER:
            return '[0-9]+'


class DLineEdit(QLineEdit):
    """Custom input field with application's standards."""

    def __init__(self, parent: QWidget, x_pos: int, y_pos: int, validator: Validators = None):
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
    """Custom date selector with application's standards."""

    def __init__(self, parent: QWidget, x_pos: int, y_pos: int):
        super().__init__(parent=parent)
        self.move(x_pos, y_pos)
        self.setFont(QFont('Ubuntu', 16))
