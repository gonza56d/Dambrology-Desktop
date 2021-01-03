import sys
from datetime import date

from PyQt5.QtWidgets import QWidget, QLabel

from business.numerology import Numerology
from models.persons import Person
from resources.components.buttons import DButton
from resources.components.inputs import DLineEdit, Validators, DCalendar
from resources.components.labels import DLabel, DPersonLabel
from resources.constants import app_constants
from resources.constants.labels import FormattedLabels, Labels


class NewStudyWindow(QWidget):
    """Window to perform a new numerologic study.
    Get all the required data from its inputs and send a Person instance to the business layer to get results."""

    person = None  # Person class instance generated on btn_calculate.click()
    lbl_names = None  # Label to indicate names input field
    input_names = None   # str to populate person.names
    lbl_last_names = None  # Label to indicate last_names input field
    input_last_names = None  # str to populate person.last_names
    lbl_birthday = None  # Label to indicate birthday date selector
    input_birthday = None  # datetime.date to indicate person.birthday
    btn_calculate = None  # Button to generate the Person instance and send it to the business layer
    # labels to indicate person numerology attributes result after btn_calculate.click()
    lbl_person = None
    lbl_person_birthday = None
    lbl_essence = None
    lbl_image = None
    lbl_destiny = None
    lbl_path = None
    lbl_karmas = None

    def __init__(self, app):
        super().__init__()
        self.setWindowTitle(Labels.DAMBROLOGY.value + ' | ' + Labels.NEW_STUDY.value)
        screen = app.primaryScreen()
        size = screen.size()
        self.setGeometry(size.width() / 2 - app_constants.APP_WIDTH / 2, size.height() / 2 - app_constants.APP_HEIGHT / 2,
                         app_constants.APP_WIDTH, app_constants.APP_HEIGHT)
        self.setFixedSize(app_constants.APP_WIDTH, app_constants.APP_HEIGHT)
        self.set_labels()
        self.init_person_labels()
        self.set_inputs()
        self.set_buttons()
        self.show()
        sys.exit(app.exec_())

    def set_labels(self):
        """Initialize window (self) labels."""
        init_height = app_constants.TOP_MARGIN
        self.lbl_names = DLabel(value=FormattedLabels.NAMES, parent=self, x_pos=app_constants.LEFT_MARGIN,
                                y_pos=init_height)
        self.lbl_last_names = DLabel(value=FormattedLabels.LAST_NAMES, parent=self, x_pos=app_constants.LEFT_MARGIN,
                                     y_pos=init_height+100)
        self.lbl_birthday = DLabel(value=FormattedLabels.BIRTHDAY, parent=self, x_pos=app_constants.LEFT_MARGIN,
                                   y_pos=init_height+200)

    def set_inputs(self):
        """Initialize window (self) input fields."""
        init_height = app_constants.TOP_MARGIN + 40
        self.input_names = DLineEdit(parent=self, x_pos=app_constants.LEFT_MARGIN, y_pos=init_height,
                                     validator=Validators.TEXT)
        self.input_last_names = DLineEdit(parent=self, x_pos=app_constants.LEFT_MARGIN, y_pos=init_height + 100,
                                          validator=Validators.TEXT)
        self.input_birthday = DCalendar(parent=self, x_pos=app_constants.LEFT_MARGIN, y_pos=init_height + 200)

    def set_buttons(self):
        """Initialize window (self) buttons."""
        self.btn_calculate = DButton(parent=self, text=Labels.CALCULATE, x_pos=app_constants.APP_WIDTH / 2 - 35,
                                     y_pos=app_constants.APP_HEIGHT - 70)

    def calculate(self):
        """Generate new Person instance and populate attributes with corresponding input field values."""
        d = self.input_birthday.selectedDate().getDate()  # date selector value as tuple(year: int, mont: int, day: int)
        d = date(d[0], d[1], d[2])
        self.person = Person()
        self.person.names = self.input_names.text()
        self.person.last_names = self.input_last_names.text()
        self.person.birthday = d
        self.person = Numerology.perform_numerology(person=self.person)
        self.set_person_labels()
        self.update()

    def set_person_labels(self):
        self.lbl_person.setText(f'<h1>{self.person.full_name}</h1>')
        self.lbl_person_birthday.setText(f'<h3>Nacimiento: {self.person.formatted_birthday}</h3>')
        self.lbl_essence.setText(f'<h3>Esencia: {self.person.essence}</h3>')
        self.lbl_image.setText(f'<h3>Imagen: {self.person.image}</h3>')
        self.lbl_destiny.setText(f'<h3>Destino: {self.person.destiny}</h3>')
        self.lbl_path.setText(f'<h3>Sendero: {self.person.path}</h3>')
        self.lbl_karmas.setText(f'<h3>Karmas: {self.person.karmas}</h3>')

    def init_person_labels(self):
        self.lbl_person = DPersonLabel(value='', parent=self, x_pos=app_constants.LEFT_MARGIN + 300,
                                       y_pos=app_constants.TOP_MARGIN, big=True)
        self.lbl_person_birthday = DPersonLabel(value='', parent=self, x_pos=app_constants.LEFT_MARGIN + 300,
                                                y_pos=app_constants.TOP_MARGIN + 40)
        self.lbl_essence = DPersonLabel(value='', parent=self, x_pos=app_constants.LEFT_MARGIN + 300,
                                        y_pos=app_constants.TOP_MARGIN + 80)
        self.lbl_image = DPersonLabel(value='', parent=self, x_pos=app_constants.LEFT_MARGIN + 300,
                                      y_pos=app_constants.TOP_MARGIN + 120)
        self.lbl_destiny = DPersonLabel(value='', parent=self, x_pos=app_constants.LEFT_MARGIN + 300,
                                        y_pos=app_constants.TOP_MARGIN + 160)
        self.lbl_path = DPersonLabel(value='', parent=self, x_pos=app_constants.LEFT_MARGIN + 450,
                                     y_pos=app_constants.TOP_MARGIN + 80)
        self.lbl_karmas = DPersonLabel(value='', parent=self, x_pos=app_constants.LEFT_MARGIN + 450,
                                       y_pos=app_constants.TOP_MARGIN + 120, big=True)
