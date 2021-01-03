from business.exceptions import BusinessException
from models.persons import Person


class Numerology:

    @staticmethod
    def perform_numerology(person: Person):
        if not isinstance(person, Person):
            raise BusinessException("Expected parameter 'person' as instance of <class 'models.persons.Person'>")
        pass
