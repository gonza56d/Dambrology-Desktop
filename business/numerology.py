from business.exceptions import BusinessException
from models.persons import Person


class Numerology:

    @classmethod
    def perform_numerology(cls, person):
        if not isinstance(person, Person):
            raise BusinessException("Expected parameter 'person' as instance of <class 'models.persons.Person'>")
        pass
