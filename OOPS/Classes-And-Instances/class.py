class Employee:     #no attributes defined yet
    def __init__(self, first, last, pay):       #cconstructor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # method to display full name of employee
    def fullname():
        return '{} {}'.format(self.first, self.last)
# The instance is passed automatically

emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

# print(emp_1)
# print(emp_2)


# print(emp_1.email)
# print(emp_2.email)

# # ability to display full name of employee
# print('{} {}'.format(emp_1.first, emp_1.last))
# print('{} {}'.format(emp_2.first, emp_2.last))


# If we left the parenthesis empty, it will give an error because the instance is passed automatically to the method. So we need to pass the instance as an argument to the method.
print(emp_1.fullname())
# print(emp_2.fullname())

