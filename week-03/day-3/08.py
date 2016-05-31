# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(self.first_name, self.last_name)

class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        sum_grades = 0
        for i in self.grades:
            sum_grades += i
        return(sum_grades / len(self.grades))

    def salute(self):
        self.greet()
        print(self.average())

tibi = Student('Tibi', 'Atya')
tibi.greet()
tibi.add_grade(5)
tibi.add_grade(2)
tibi.add_grade(4)
tibi.add_grade(5)
tibi.salute()
