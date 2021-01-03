from PyQt5.QtWidgets import QLabel, QWidget

from business.exceptions import DambrologyGuiException
from resources.constants.labels import BaseLabel


class DLabel(QLabel):

    text = ''

    def __init__(self, value: BaseLabel, parent: QWidget, x_pos: int, y_pos: int):
        if not isinstance(value, BaseLabel):
            raise DambrologyGuiException(
                "Expected parameter 'value' as <enum 'resources.constants.labels.FormattedLabels'> "
                "or <enum 'resources.constants.labels.Labels'>")
        self.text = value.value
        super().__init__(self.text, parent=parent)
        self.move(x_pos, y_pos)


class DPersonLabel(QLabel):

    def __init__(self, value: str, parent: QWidget, x_pos: int, y_pos: int):
        super().__init__(value, parent=parent)
        self.move(x_pos, y_pos)
        self.setFixedHeight(80)
        self.setFixedWidth(400)
