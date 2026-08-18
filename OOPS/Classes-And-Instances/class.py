class Employee:     # Defines a class named Employee; this acts as a blueprint for employee objects

    def __init__(self, first, last, pay):     # Constructor method; runs automatically whenever a new Employee object is created
        self.first = first                   # Stores the first name in the current object's 'first' instance variable
        self.last = last                     # Stores the last name in the current object's 'last' instance variable
        self.pay = pay                       # Stores the salary in the current object's 'pay' instance variable
        self.email = first + '.' + last + '@company.com'  # Creates an email address using the first and last names

    # Method to display the full name of the employee
    def fullname(self):                      # Defines an instance method; 'self' refers to the current Employee object
        return '{} {}'.format(self.first, self.last)  # Returns the first and last name together as a full name


# Creating the first Employee object
emp_1 = Employee('John', 'Doe', 50000)
# Python automatically calls __init__() and passes emp_1 as 'self'
# self.first = 'John'
# self.last = 'Doe'
# self.pay = 50000
# self.email = 'John.Doe@company.com'


# Creating the second Employee object
emp_2 = Employee('Jane', 'Smith', 60000)
# Python automatically calls __init__() and passes emp_2 as 'self'
# self.first = 'Jane'
# self.last = 'Smith'
# self.pay = 60000
# self.email = 'Jane.Smith@company.com'


# print(emp_1)
# Prints the emp_1 object itself.
# Without defining __str__() or __repr__(), Python displays the object's default representation.


# print(emp_2)
# Prints the emp_2 object itself.
# Again, it displays the default object representation because __str__() or __repr__() is not defined.


# print(emp_1.email)
# Accesses and prints the email instance variable of emp_1.
# Output: John.Doe@company.com


# print(emp_2.email)
# Accesses and prints the email instance variable of emp_2.
# Output: Jane.Smith@company.com


# print('{} {}'.format(emp_1.first, emp_1.last))
# Accesses emp_1's first and last instance variables
# and combines them to display the employee's full name.
# Output: John Doe


# print('{} {}'.format(emp_2.first, emp_2.last))
# Accesses emp_2's first and last instance variables
# and combines them to display the employee's full name.
# Output: Jane Smith


# Calling the fullname() method using the emp_1 object
print(emp_1.fullname())
# Python automatically passes emp_1 as the 'self' argument.
# This is internally similar to:
# Employee.fullname(emp_1)
#
# The method accesses:
# self.first -> emp_1.first -> 'John'
# self.last  -> emp_1.last  -> 'Doe'
#
# Output: John Doe


# Calling the fullname() method directly through the class
Employee.fullname(emp_1)
# Here, we call fullname() using the Employee class instead of the object.
# Since Python does NOT automatically know which instance to use here,
# we explicitly pass emp_1 as the argument.
#
# This is equivalent to:
# emp_1.fullname()
#
# NOTE: This line returns 'John Doe' but does NOT display it,
# because we have not used print().
#
# To display it, we would write:
# print(Employee.fullname(emp_1))


# print(emp_2.fullname())
# Calls fullname() for the emp_2 object.
# Python automatically passes emp_2 as 'self'.
# Output: Jane Smith