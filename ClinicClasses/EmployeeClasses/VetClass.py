from BaseEmployeeClass import Employee


class Veterinarian(Employee):

    salary: int

    def __init__(self, sal, fname, mname, lname, phone_number):
        super().__init__(self, fname, mname, lname, phone_number)
        self.salary = sal
