class Employee:

    # Class variable
    # Shared by all instances of the Employee class
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # Instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # Instance method to display the full name
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Instance method to apply the salary raise
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Creating two Employee objects
emp1_ = Employee('Corey', 'Schafer', 50000)
emp2_ = Employee('Test', 'User', 60000)


# ---------------------------------------------------------
# Accessing instance variables
# ---------------------------------------------------------

# print(emp1_.email)
# Output: Corey.Schafer@company.com

# print(emp2_.email)
# Output: Test.User@company.com


# ---------------------------------------------------------
# Applying the raise
# ---------------------------------------------------------

# emp1_.apply_raise()
# emp1_'s salary changes from 50000 to 52000
#
# Calculation:
# 50000 * 1.04 = 52000

# print(emp1_.pay)
# Output: 52000


# ---------------------------------------------------------
# Creating an instance variable with the same name
# as the class variable
# ---------------------------------------------------------

emp1_.raise_amount = 1.05

# IMPORTANT:
# This does NOT change the class variable.
#
# Employee.raise_amount is still 1.04.
#
# Instead, Python creates a new instance variable
# called raise_amount specifically for emp1_.


# ---------------------------------------------------------
# Checking emp1_'s instance variables
# ---------------------------------------------------------

print(emp1_.__dict__)

# __dict__ shows the attributes stored directly
# inside the emp1_ object.
#
# It will contain something similar to:
#
# {
#     'first': 'Corey',
#     'last': 'Schafer',
#     'pay': 50000,
#     'email': 'Corey.Schafer@company.com',
#     'raise_amount': 1.05
# }


# ---------------------------------------------------------
# Accessing raise_amount
# ---------------------------------------------------------

print(emp1_.raise_amount)
# Output: 1.05
#
# Python first checks emp1_.
# emp1_ has its own raise_amount = 1.05.
# Therefore, Python uses 1.05.


print(emp2_.raise_amount)
# Output: 1.04
#
# emp2_ does not have its own raise_amount.
# Python therefore looks at the Employee class
# and uses Employee.raise_amount = 1.04.


print(Employee.raise_amount)
# Output: 1.04
#
# This directly accesses the class variable.
# It has not been changed by emp1_.raise_amount = 1.05.


# ---------------------------------------------------------
# Checking the class dictionary
# ---------------------------------------------------------

# print(Employee.__dict__)

# Employee.__dict__ shows attributes that belong
# directly to the Employee class.
#
# It includes:
# - raise_amount
# - __init__
# - fullname
# - apply_raise
#
# It does not contain emp1_'s instance-specific variables.


# =========================================================
# ATTRIBUTE LOOKUP
# =========================================================

# When we write:
#
# emp1_.raise_amount
#
# Python first checks the emp1_ object.
#
# If raise_amount exists inside emp1_:
#     Python uses emp1_'s value.
#
# Otherwise:
#     Python looks inside the Employee class.
#
#
# For emp1_:
#
# emp1_.raise_amount
#        ↓
# Found inside emp1_
#        ↓
# 1.05
#
#
# For emp2_:
#
# emp2_.raise_amount
#        ↓
# Not found inside emp2_
#        ↓
# Check Employee class
#        ↓
# 1.04


# =========================================================
# CLASS VARIABLE vs INSTANCE VARIABLE
# =========================================================

# Class variable:
#
#     Employee.raise_amount = 1.04
#
# Shared by all Employee objects.


# Instance variable:
#
#     emp1_.raise_amount = 1.05
#
# Belongs only to emp1_.


# Final values:
#
# Employee.raise_amount  -> 1.04
# emp1_.raise_amount     -> 1.05
# emp2_.raise_amount     -> 1.04