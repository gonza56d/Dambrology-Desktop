from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QWidget

from business.exceptions import DambrologyGuiException
from resources.constants.labels import Labels


class DButton(QPushButton):
    """Custom button with application's standards."""

    text = ''

    def __init__(self, parent: QWidget, text: Labels, x_pos: int, y_pos: int):
        if not isinstance(text, Labels):
            raise DambrologyGuiException(
                "Expected parameter 'text' as <enum 'resources.constants.labels.Labels'>")
        super().__init__(parent=parent)
        self.move(x_pos, y_pos)
        self.text = text.value
        self.setText(self.text)
        self.setFont(QFont('Ubuntu', 22))
        self.clicked.connect(lambda: self.on_click())

    def on_click(self):
        self.parent().calculate()
