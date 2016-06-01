# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016
class Person(object):
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        if self.birth_date < 0 or self.birth_date > 2016:
            raise ValueError('The date of birth must be between 0 and 2016')
