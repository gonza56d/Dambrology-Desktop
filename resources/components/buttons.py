from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton

from business.exceptions import DambrologyGuiException
from resources.constants.labels import FormattedLabels, Labels


class DButton(QPushButton):

    text = ''

    def __init__(self, parent, text, x_pos, y_pos):
        if not isinstance(text, FormattedLabels) and not isinstance(text, Labels):
            raise DambrologyGuiException(
                "Expected parameter 'text' as <enum 'resources.constants.labels.Labels'>")
        super().__init__(parent=parent)
        self.move(x_pos, y_pos)
        self.text = text.value
        self.setText(self.text)
        self.setFont(QFont('Ubuntu', 22))
