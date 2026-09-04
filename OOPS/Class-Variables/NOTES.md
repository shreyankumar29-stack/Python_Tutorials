# Python OOP — Part 2

## Class Variables

---

## 1. What are Class Variables?

A **class variable** is a variable that is shared among **all instances (objects) of a class**.

Example:

```python
class Employee:

    raise_amount = 1.04
```

Here:

```python
raise_amount
```

is a **class variable**.

It belongs to the class rather than a particular object.

---

# 2. Instance Variables vs Class Variables

### Instance Variable

An instance variable is unique to each object.

```python
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
```

Here:

```python
self.first
self.last
self.pay
```

are instance variables.

Different objects can have different values.

---

### Class Variable

A class variable is shared by all instances.

```python
class Employee:

    raise_amount = 1.04
```

All employees initially use:

```text
1.04
```

---

# 3. Complete Example

```python
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
```

Create objects:

```python
emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Jane", "Doe", 60000)
```

Both objects can access the class variable:

```python
print(emp_1.raise_amount)
print(emp_2.raise_amount)
```

Output:

```text
1.04
1.04
```

The class itself can also access it:

```python
print(Employee.raise_amount)
```

Output:

```text
1.04
```

---

# 4. Using Class Variables in Methods

We can use a class variable inside an instance method.

```python
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
```

Now:

```python
emp_1 = Employee("John", "Doe", 50000)

emp_1.apply_raise()

print(emp_1.pay)
```

The salary is increased using:

```python
self.raise_amount
```

---

# 5. Why Use Class Variables?

Class variables are useful when a value should be **common/shared across all objects**.

For example:

```python
raise_amount = 1.04
```

If every employee should initially receive the same raise percentage, it makes sense to store it as a class variable.

Other examples:

```python
company_name = "ABC Company"
tax_rate = 0.18
interest_rate = 0.07
```

---

# 6. Accessing Class Variables

A class variable can be accessed using either:

```python
Employee.raise_amount
```

or:

```python
emp_1.raise_amount
```

Example:

```python
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
```

All can return:

```text
1.04
```

---

# 7. Attribute Lookup

When Python sees:

```python
emp_1.raise_amount
```

it first checks whether `raise_amount` exists inside the **instance**.

If it doesn't find it there, Python checks the **class**.

Conceptually:

```text
emp_1
  ↓
Instance attributes
  ↓
Employee class
  ↓
Parent classes
```

So if `raise_amount` is not inside `emp_1`, Python finds it in `Employee`.

---

# 8. `__dict__`

Every object has an attribute dictionary called:

```python
__dict__
```

Example:

```python
print(emp_1.__dict__)
```

You might get:

```python
{
    'first': 'John',
    'last': 'Doe',
    'pay': 50000
}
```

Notice that:

```python
raise_amount
```

is not present.

That's because it is a **class variable**, not an instance variable.

Check the class:

```python
print(Employee.__dict__)
```

You will find:

```python
'raise_amount': 1.04
```

---

# 9. Changing a Class Variable

We can change the class variable through the class:

```python
Employee.raise_amount = 1.05
```

Now:

```python
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
```

Output:

```text
1.05
1.05
1.05
```

Because both objects look up the value from the class.

---

# 10. Changing a Class Variable Through an Instance

Be careful with this:

```python
emp_1.raise_amount = 1.05
```

This does **not** change the class variable.

Instead, Python creates an **instance variable** called `raise_amount` for `emp_1`.

Now:

```python
print(emp_1.__dict__)
```

will contain:

```python
{
    'first': 'John',
    'last': 'Doe',
    'pay': 50000,
    'raise_amount': 1.05
}
```

---

# 11. What Happens to Other Objects?

Suppose:

```python
emp_1.raise_amount = 1.05
```

Then:

```python
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
```

Output:

```text
1.05
1.04
1.04
```

Why?

Because:

```python
emp_1.raise_amount
```

finds the value in `emp_1` itself.

But:

```python
emp_2.raise_amount
```

doesn't have its own `raise_amount`, so Python finds the class variable.

---

# 12. Important Difference

### This:

```python
Employee.raise_amount = 1.05
```

changes the **class variable**.

### While this:

```python
emp_1.raise_amount = 1.05
```

creates/changes an **instance variable**.

This distinction is extremely important.

---

# 13. Counting Number of Employees

Class variables can also be used for keeping track of information shared by the class.

Example:

```python
class Employee:

    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1
```

Now:

```python
emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Jane", "Doe", 60000)
```

Check:

```python
print(Employee.num_of_emps)
```

Output:

```text
2
```

---

# 14. Why Use `Employee.num_of_emps`?

Inside:

```python
__init__()
```

we write:

```python
Employee.num_of_emps += 1
```

rather than:

```python
self.num_of_emps += 1
```

because we want to modify the **shared class variable**.

If we used:

```python
self.num_of_emps
```

we could accidentally create an instance variable.

---

# 15. Complete Class Variable Example

```python
class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
```

Usage:

```python
emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Jane", "Doe", 60000)

print(Employee.num_of_emps)
```

Output:

```text
2
```

---

# 16. Instance Variables

Instance variables belong to a specific object.

Example:

```python
emp_1.first
emp_1.last
emp_1.pay
```

and:

```python
emp_2.first
emp_2.last
emp_2.pay
```

can have different values.

---

# 17. Class Variables

Class variables belong to the class and are generally shared.

Example:

```python
Employee.raise_amount
Employee.num_of_emps
```

---

# 18. Quick Comparison

| Instance Variable             | Class Variable                      |
| ----------------------------- | ----------------------------------- |
| Belongs to an object          | Belongs to the class                |
| Usually created using `self`  | Defined directly inside class       |
| Different for each object     | Shared by objects unless overridden |
| Example: `self.pay`           | Example: `raise_amount`             |
| Stored in instance `__dict__` | Stored in class `__dict__`          |

---

# 19. Important Rules

### Rule 1

```python
self.variable
```

usually refers to an **instance variable**.

---

### Rule 2

```python
ClassName.variable
```

accesses the **class variable**.

---

### Rule 3

If an instance doesn't have an attribute, Python searches the class.

```python
emp_1.raise_amount
```

If `emp_1` doesn't contain `raise_amount`, Python looks in:

```python
Employee
```

---

### Rule 4

Doing:

```python
emp_1.raise_amount = 1.05
```

can create an instance attribute instead of changing the class attribute.

---

# 20. Key Example to Remember

```python
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
```

Here:

```text
Employee
│
├── raise_amount       ← Class Variable
│
├── emp_1
│   ├── first          ← Instance Variable
│   ├── last           ← Instance Variable
│   └── pay            ← Instance Variable
│
└── emp_2
    ├── first          ← Instance Variable
    ├── last           ← Instance Variable
    └── pay            ← Instance Variable
```

---

# 21. Interview Questions

### Q1. What is a class variable?

A variable shared by instances of a class.

---

### Q2. How do you define a class variable?

Define it directly inside the class, outside methods.

```python
class Employee:
    raise_amount = 1.04
```

---

### Q3. How do you define an instance variable?

Usually using `self` inside `__init__()`:

```python
self.pay = pay
```

---

### Q4. What is `__dict__`?

`__dict__` contains the attributes stored for an object or class.

Example:

```python
print(emp_1.__dict__)
```

---

### Q5. What happens when an instance accesses a class variable?

Python first looks for the attribute in the instance. If it isn't there, it looks in the class.

---

### Q6. What is the difference between these?

```python
Employee.raise_amount = 1.05
```

and:

```python
emp_1.raise_amount = 1.05
```

First one changes the **class variable**.

Second one creates/changes an **instance variable** for `emp_1`.

---

# 22. Summary

```text
INSTANCE VARIABLE
        ↓
    self.variable
        ↓
Belongs to individual object


CLASS VARIABLE
        ↓
    Class.variable
        ↓
Shared by instances


ATTRIBUTE LOOKUP
        ↓
Instance → Class → Parent Class
```

### Most Important Things to Remember

```python
self.pay
```

→ Instance variable

```python
Employee.raise_amount
```

→ Class variable

```python
emp_1.raise_amount
```

→ Python first checks `emp_1`, then the class

```python
emp_1.raise_amount = 1.05
```

→ Creates/changes an instance attribute

```python
Employee.raise_amount = 1.05
```

→ Changes the class attribute
