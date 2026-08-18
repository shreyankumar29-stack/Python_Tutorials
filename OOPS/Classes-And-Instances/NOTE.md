## OOPS CONCEPT

## Why should we use class?
They allow us logically group our data and functions in a way that's easy to reuse and also easy to build upon of needed to be.

## methods: 
function associaated with the class

## NOTE:
 instance variable contain data that is unique to each instance

## Common Mistake:
When creating methods we forget the self argument for the instance

**Example**
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

PS C:\Users\Shreyansh kumar\Documents\PYTHON\OOPS\Classes-And-Instances> python class.py
Traceback (most recent call last):
  File "C:\Users\Shreyansh kumar\Documents\PYTHON\OOPS\Classes-And-Instances\class.py", line 29, in <module>
    print(emp_1.fullname())
          ~~~~~~~~~~~~~~^^
TypeError: Employee.fullname() takes 0 positional arguments but 1 was given