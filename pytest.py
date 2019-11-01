if __name__ == "__main__":

    class Employee:

        num_of_employees = 0

        def __init__(self, first, last, salary, performance_rating):
            self.first = first
            self.last = last
            self.salary = salary
            self.email = first + "." + last + "@company.com"
            self.performance_rating = performance_rating
            Employee.num_of_employees += 1

        def fullname(self):
            return '{} {}'.format(self.first, self.last)

        def merit_raise_strategy(self):
            if self.performance_rating == 1:
                return self.salary * 1.05
            elif self.performance_rating == 2:
                return self.salary * 1.03
            elif self.performance_rating == 3:
                return self.salary * 1.00

    employee_1 = Employee('Average', 'Employee', 70000, 2)
    print(employee_1.fullname() + "'s new salary is: $" +
          str(employee_1.merit_raise_strategy()) + " USD")

    employee_2 = Employee('Stellar', "Employee", 70000, 1)
    print(employee_2.fullname() + "'s new salary is: $" +
          str(employee_2.merit_raise_strategy()) + " USD")

    employee_3 = Employee('Grumpy', "Pants", 70000, 3)
    print(employee_3.fullname() + "'s new salary is: $" +
          str(employee_3.merit_raise_strategy()) + " USD")

    print("Total number of employees in the system: " +
          str(Employee.num_of_employees))
