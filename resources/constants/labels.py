from enum import Enum


class Labels(Enum):

    DAMBROLOGY = 'Dambrology'
    NEW_STUDY = 'Nuevo Estudio'
    CALCULATE = 'Calcular'


class FormattedLabels(Enum):

    NAMES = '<h1>Nombres:</h1>'
    LAST_NAMES = '<h1>Apellidos:</h1>'
    BIRTHDAY = '<h1>Nacimiento:</h1>'
