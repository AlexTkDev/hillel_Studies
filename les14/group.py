from ERROR_MaxAmountException import MaxAmountException


class Group:

    def __init__(self, number):
        self.counter = None
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.counter = 0
        for _ in self.group:
            self.counter += 1

        if self.counter == 10:
            raise MaxAmountException(
                "Max Amount Students Exceeded", student.last_name, student.first_name)
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__()
        return f'Number:{self.number}\n{all_students}'