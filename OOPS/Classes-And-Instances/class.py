class Employee:     #no attributes defined yet
    def __init__(self, first, last, pay):       #cconstructor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

# The instance is passed automatically

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'John'
emp_1.last = 'Doe'
emp_1.email = 'john.doe@company.com'
emp_1.pay = 50000

emp_2.first = 'Jane'
emp_2.last = 'Smith'
emp_2.email = 'jane.smith@company.com'
emp_2.pay = 60000


print(emp_1.email)
print(emp_2.email)

