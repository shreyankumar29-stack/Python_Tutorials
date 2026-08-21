## Class Variables: Variables that are shared among all instances of a class

class Employee:

    # Class variable.
    # This variable belongs to the class itself and is shared by all
    # instances unless an instance has its own variable with the same name.
    raise_amount = 1.04

    # Constructor method.
    # It runs automatically whenever a new Employee object is created.
    def __init__(self, first, last, pay):

        # Instance variable containing the employee's first name.
        self.first = first

        # Instance variable containing the employee's last name.
        self.last = last

        # Instance variable containing the employee's salary.
        self.pay = pay

        # Instance variable containing the employee's email address.
        self.email = first + '.' + last + '@company.com'

    # Instance method used to return the employee's full name.
    def fullname(self):

        # self refers to the current Employee object.
        # self.first and self.last access that object's instance variables.
        return '{} {}'.format(self.first, self.last)

    # Instance method used to increase the employee's salary.
    def apply_raise(self):

        # self.raise_amount accesses the raise_amount value.
        #
        # If the instance has its own raise_amount variable,
        # Python uses that value.
        #
        # Otherwise, Python looks at the Employee class and uses
        # the class variable raise_amount = 1.04.
        self.pay = int(self.pay * self.raise_amount)


# Creating the first Employee object.
# first = 'Corey'
# last = 'Schafer'
# pay = 50000
emp1_ = Employee('Corey', 'Schafer', 50000)


# Creating the second Employee object.
# first = 'Test'
# last = 'User'
# pay = 60000
emp2_ = Employee('Test', 'User', 60000)


# print(emp1_.email)
# Accesses the email instance variable of emp1_.
# Output:
# Corey.Schafer@company.com


# emp1_.apply_raise()
# Calls the apply_raise() method for emp1_.
#
# Since emp1_ does not have its own raise_amount variable,
# Python looks for raise_amount in the Employee class.
#
# Employee.raise_amount = 1.04
#
# New salary:
# 50000 * 1.04 = 52000


# print(emp2_.email)
# Accesses the email instance variable of emp2_.
# Output:
# Test.User@company.com


# Creating an instance variable named raise_amount specifically
# for emp1_.
#
# IMPORTANT:
# This does NOT change Employee.raise_amount.
# It only creates a new variable inside emp1_.
emp1_.raise_amount = 1.05


# __dict__ shows the instance variables stored directly inside emp1_.
#
# It will contain:
# first
# last
# pay
# email
# raise_amount
#
# Notice that raise_amount now appears here because we created
# an instance-specific raise_amount for emp1_.
print(emp1_.__dict__)


# Python first checks whether emp1_ has its own raise_amount.
# emp1_ does have one:
# raise_amount = 1.05
#
# Therefore, the output is:
# 1.05
print(emp1_.raise_amount)


# emp2_ does NOT have its own raise_amount.
#
# Python therefore looks at the Employee class and finds:
# raise_amount = 1.04
#
# Output:
# 1.04
print(emp2_.raise_amount)


# Accessing the class variable directly through the class.
#
# This does not depend on any particular employee instance.
# It directly accesses Employee's raise_amount.
#
# Output:
# 1.04
print(Employee.raise_amount)


# print(Employee.__dict__)
# __dict__ displays the attributes and methods defined
# directly inside the Employee class.
#
# It will show class-level information such as:
# raise_amount
# __init__
# fullname
# apply_raise
#
# It will NOT show emp1_'s instance variables because those
# belong to the object, not to the class.


# ============================================================
# IMPORTANT CONCEPT
# ============================================================

# Initially:
#
# Employee.raise_amount = 1.04
# emp1_ does not have raise_amount
# emp2_ does not have raise_amount
#
# Therefore:
#
# emp1_.raise_amount  -> 1.04
# emp2_.raise_amount  -> 1.04
# Employee.raise_amount -> 1.04


# After:
#
# emp1_.raise_amount = 1.05
#
# Python creates a NEW instance variable inside emp1_.
#
# It does NOT modify the class variable.
#
# Therefore:
#
# emp1_.raise_amount      -> 1.05
# emp2_.raise_amount      -> 1.04
# Employee.raise_amount   -> 1.04


# ============================================================
# ATTRIBUTE LOOKUP
# ============================================================

# When we write:
#
# emp1_.raise_amount
#
# Python first checks the emp1_ object.
#
# If raise_amount exists there:
#     Use emp1_'s value.
#
# If it does not exist:
#     Look inside the Employee class.
#
# This is why emp1_ can have 1.05 while emp2_ still has 1.04.