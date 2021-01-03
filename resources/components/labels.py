from PyQt5.QtWidgets import QLabel

from business.exceptions import DambrologyGuiException
from resources.constants.labels import FormattedLabels, Labels


class DLabel(QLabel):

    text = ''

    def __init__(self, value, parent, x_pos, y_pos):
        if not isinstance(value, FormattedLabels) and not isinstance(value, Labels):
            raise DambrologyGuiException(
                "Expected parameter 'value' as <enum 'resources.constants.labels.FormattedLabels'> "
                "or <enum 'resources.constants.labels.Labels'>")
        self.text = value.value
        super().__init__(self.text, parent=parent)
        self.move(x_pos, y_pos)
