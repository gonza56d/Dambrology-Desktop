from enum import Enum

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit

from resources.exceptions import DambrologyGuiException


class Validator(Enum):
    TEXT = 'TEXT'
    NUMBER = 'NUMBER'

    @classmethod
    def regex_type(cls, validator):
        if validator is cls.TEXT:
            return '[a-z-A-Z_]+'
        elif validator is cls.NUMBER:
            return '[0-9]+'


class GLineEdit(QLineEdit):

    def __init__(self, parent, x_pos, y_pos, validator=None):
        super().__init__(parent=parent)
        self.move(x_pos, y_pos)
        if validator:
            if not isinstance(validator, Validator):
                raise DambrologyGuiException("Expected parameter 'validator' as components.inputs.Validator")
            regex = QRegExp(Validator.regex_type(validator))
            validator = QRegExpValidator(regex)
            self.setValidator(validator)
