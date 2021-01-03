from datetime import date

from business.exceptions import BusinessException
from models.persons import Person


class Numerology:
    """Controller class that holds all the logic to perform Numerology to a person."""

    VOWELS = 'aeiouAEIOU'
    MASTER_NUMBERS = (11, 22, 33)
    KARMA_NUMBERS = (13, 14, 16, 19)
    person = None

    @classmethod
    def perform_numerology(cls, person: Person):
        """Calculate and set numerology numbers for the Person instance received and return the same object with the
        calculated values."""
        if not isinstance(person, Person):
            raise BusinessException("Expected parameter 'person' as instance of <class 'models.persons.Person'>")
        cls.person = person
        complete_name = person.names.split(' ') + person.last_names.split(' ')
        person.essence = Numerology.get_essence(complete_name)
        person.image = Numerology.get_image(complete_name)
        person.destiny = Numerology.get_destiny(complete_name)
        person.path = Numerology.get_path(person.birthday)
        return person

    @staticmethod
    def pair(number: int):
        return number % 2 == 0

    @staticmethod
    def vowel(letter: str):
        return letter in Numerology.VOWELS

    @staticmethod
    def make_return(numbers: list):
        """Finally add all the numbers obtained from each name into a single one."""
        ret = 0
        for n in numbers:
            ret += n
        return Numerology.reduce(ret)

    @staticmethod
    def get_path(birthday: date):
        """Calculate path number by splitting birthday in year-month-day numbers, adding digits and reducing each the
        results, and then adding the results final results of the splitted parts and reducing it.
        E.G: 1996-7-1 -> 25-7-1 -> 7-7-1 -> 15 -> 6"""
        str_date_list = str(birthday).split('-')
        numbers = []
        for part in str_date_list:
            value = 0
            for number in part:
                value += int(number)
            value = Numerology.reduce(value)
            numbers.append(value)
        return Numerology.make_return(numbers)

    @staticmethod
    def get_essence(names: list):
        """Calculate essence number by adding all the numeric values of only vowel letters from each name separately,
        and later adding these separated results into one."""
        numbers = []
        for name in names:
            value = 0
            for letter in name:
                if Numerology.vowel(letter):
                    value += Numerology.get_letter_value(letter)
            value = Numerology.reduce(value)
            numbers.append(value)
        return Numerology.make_return(numbers)

    @staticmethod
    def get_image(names: list):
        """Calculate image number by adding all the numeric values of only consonant letters from each name separately,
        and later adding these separated results into one."""
        numbers = []
        for name in names:
            value = 0
            for letter in name:
                if not Numerology.vowel(letter):
                    value += Numerology.get_letter_value(letter)
            value = Numerology.reduce(value, False)
            numbers.append(value)
        return Numerology.make_return(numbers)

    @staticmethod
    def get_destiny(names: list):
        """Calculate destiny number by adding all the numeric values of all the letters from each name separately, and
        later adding these separated results into one."""
        numbers = []
        for name in names:
            value = 0
            for letter in name:
                value += Numerology.get_letter_value(letter)
            value = Numerology.reduce(value)
            numbers.append(value)
        return Numerology.make_return(numbers)

    @classmethod
    def check_append_karma(cls, number: int):
        if number in Numerology.KARMA_NUMBERS:
            cls.person.karmas.append(number)

    @staticmethod
    def reduce(number: int, check_karma: bool = True):
        """Reduce any number greather than 9 and not master by adding its own digits.
        EG: number = 24 -> 2 + 4 -> number = 6"""
        while number > 9 and not Numerology.master_number(number):
            if check_karma:
                Numerology.check_append_karma(number)
            result = 0
            for n in str(number):
                result += int(n)
            number = result
        return number

    @staticmethod
    def master_number(number: int):
        """Master numbers are 11, 22, and 33, and they are not reducible."""
        return number in Numerology.MASTER_NUMBERS

    @staticmethod
    def get_letter_value(letter):
        """Return the numeric value of each letter according Numerology."""
        letter = letter.lower()
        if letter in 'ajs':
            return 1
        elif letter in 'bkt':
            return 2
        elif letter in 'clu':
            return 3
        elif letter in 'dmv':
            return 4
        elif letter in 'enw':
            return 5
        elif letter in 'fox':
            return 6
        elif letter in 'gpy':
            return 7
        elif letter in 'hqz':
            return 8
        elif letter in 'ir':
            return 9
        return 0
