class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1_ = Employee('Corey', 'Schafer', 50000)
emp2_ = Employee('Test', 'User', 60000)


# print(emp1_.email)
# emp1_.apply_raise()
# print(emp2_.email)

emp1_.raise_amount = 1.05

print(emp1_.__dict__)
#So, I can access this class variable from my class itself as well as from my instances of the class. So, let's see how we can do that.
print(emp1_.raise_amount)
print(emp2_.raise_amount)
print(Employee.raise_amount)

# print(Employee.__dict__)




#Note:if we run this code where emp1_.raise_amount = 1.05, then it will create a new instance variable for emp1_ and it will not change the class variable raise_amount. So, if we print emp1_.raise_amount, it will give us 1.05 but if we print emp2_.raise_amount, it will give us 1.04 because emp2_ is still using the class variable raise_amount.