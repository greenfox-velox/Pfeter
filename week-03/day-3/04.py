# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class student(object):
    def __init__(self):
        self.grades = []

    def add_grade(self, grade_input):
        if grade_input < 5 and grade_input > 1:
            self.grades.append(grade_input)

    def get_average(self):
        sum_grades = 0
        for i in self.grades:
            sum_grades += i
        return(sum_grades / len(self.grades))

Pistike = student()
Pistike.add_grade(2)
Pistike.add_grade(4)
Pistike.add_grade(2)
Pistike.add_grade(4)
Pistike.add_grade(2)
Pistike.add_grade(4)
print(Pistike.get_average())
