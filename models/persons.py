
class Person:

    names = ''
    last_names = ''
    birthday = None
    essence = 0
    image = 0
    destiny = 0
    path = 0
    karmas = []

    def __init__(self):
        self.karmas = []

    @property
    def full_name(self):
        """Return last names and names concatenated if it has both, or either names or last names if it has not."""
        if self.last_names and self.names:
            return f'{self.last_names}, {self.names}'
        return f'{self.names}' or f'{self.last_names}'

    @property
    def formatted_birthday(self):
        if self.birthday is not None:
            return f'{self.birthday.day}/{self.birthday.month}/{self.birthday.year}'
