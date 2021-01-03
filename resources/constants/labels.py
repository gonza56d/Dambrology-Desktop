from enum import Enum


class BaseLabel(Enum):
    """Utility class to inherit from and use as type hint/validation.
    Implementations: Labels, FormattedLabels"""
    pass


class Labels(BaseLabel):
    """Common application label implementations."""

    DAMBROLOGY = 'Dambrology'
    NEW_STUDY = 'Nuevo Estudio'
    CALCULATE = 'Calcular'


class FormattedLabels(BaseLabel):
    """Application label implementations with HTML tags."""

    NAMES = '<h1>Nombres:</h1>'
    LAST_NAMES = '<h1>Apellidos:</h1>'
    BIRTHDAY = '<h1>Nacimiento:</h1>'
