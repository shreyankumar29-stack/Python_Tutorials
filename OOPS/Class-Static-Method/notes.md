# Python OOP — Part 3

## Class Methods and Static Methods

---

## 1. Class Methods

A **class method** is a method that is bound to the **class**, rather than to an individual object.

It is created using the `@classmethod` decorator.

### Syntax

```python
class Employee:

    @classmethod
    def method_name(cls):
        # code
```

Here:

* `@classmethod` → tells Python that this is a class method.
* `cls` → refers to the class itself.
* `self` is **not** used in a class method.

---

## 2. Example of Class Method

```python
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
```

Now we can call:

```python
Employee.set_raise_amount(1.05)
```

This changes the class variable:

```python
print(Employee.raise_amount)
```

Output:

```text
1.05
```

---

## 3. `cls` vs `self`

### `self`

`self` refers to the **instance/object**.

```python
def instance_method(self):
    pass
```

Example:

```python
emp_1 = Employee("John", "Doe", 50000)
```

Here:

```python
emp_1
```

is the instance.

---

### `cls`

`cls` refers to the **class**.

```python
@classmethod
def class_method(cls):
    pass
```

For:

```python
Employee.set_raise_amount(1.05)
```

`cls` refers to:

```python
Employee
```

### Quick Difference

| `self`                                          | `cls`                                          |
| ----------------------------------------------- | ---------------------------------------------- |
| Refers to object/instance                       | Refers to class                                |
| Used in instance methods                        | Used in class methods                          |
| Access instance variables                       | Access class variables                         |
| Passed automatically when called through object | Passed automatically when called through class |

---

# 4. Calling Class Methods Using an Instance

A class method can also be called using an instance.

```python
emp_1 = Employee("John", "Doe", 50000)

emp_1.set_raise_amount(1.05)
```

Python still passes the **class** as `cls`.

Therefore:

```python
emp_1.set_raise_amount(1.05)
```

and

```python
Employee.set_raise_amount(1.05)
```

both work.

---

# 5. Class Methods as Alternative Constructors

One of the most useful applications of class methods is creating **alternative constructors**.

Suppose employee information is provided as a string:

```python
emp_str_1 = "John-Doe-50000"
```

We could split it manually:

```python
first, last, pay = emp_str_1.split("-")

emp_1 = Employee(first, last, pay)
```

Instead, we can create a class method.

```python
@classmethod
def from_string(cls, emp_str):
    first, last, pay = emp_str.split("-")
    return cls(first, last, pay)
```

Now:

```python
emp_1 = Employee.from_string("John-Doe-50000")
```

This creates an `Employee` object.

---

## 6. Complete Example

```python
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
```

Usage:

```python
emp_1 = Employee.from_string("John-Doe-50000")

print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)
```

Output:

```text
John
Doe
50000
```

---

# 7. Why Use `cls` Instead of `Employee`?

We could technically write:

```python
return Employee(first, last, pay)
```

But it is better to write:

```python
return cls(first, last, pay)
```

because `cls` refers to the **actual class calling the method**.

This makes the method work properly with subclasses as well.

---

# 8. Static Methods

A **static method** is a method that does not depend on either:

* the instance (`self`)
* the class (`cls`)

It is created using:

```python
@staticmethod
```

### Syntax

```python
class Employee:

    @staticmethod
    def method_name():
        # code
```

---

# 9. Example of Static Method

Suppose we want to check whether today is a weekday.

```python
import datetime

class Employee:

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
```

Usage:

```python
my_date = datetime.date(2026, 9, 4)

print(Employee.is_workday(my_date))
```

The method doesn't need:

```python
self
```

or:

```python
cls
```

Therefore, it is a good candidate for a static method.

---

# 10. Instance Method vs Class Method vs Static Method

Python classes commonly have three types of methods.

### Instance Method

```python
def method(self):
```

Works with the **instance**.

Example:

```python
emp_1.fullname()
```

---

### Class Method

```python
@classmethod
def method(cls):
```

Works with the **class**.

Example:

```python
Employee.set_raise_amount(1.05)
```

---

### Static Method

```python
@staticmethod
def method():
```

Doesn't automatically receive either the instance or class.

Example:

```python
Employee.is_workday(date)
```

---

## 11. Quick Comparison

| Type            | Decorator       | First Argument | Used For                                          |
| --------------- | --------------- | -------------- | ------------------------------------------------- |
| Instance Method | None            | `self`         | Instance-specific operations                      |
| Class Method    | `@classmethod`  | `cls`          | Class-level operations / alternative constructors |
| Static Method   | `@staticmethod` | None           | Utility/helper functions                          |

---

# 12. Important Example

```python
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
```

---

# 13. When Should You Use Each Method?

### Use an Instance Method when:

The method needs information about a particular object.

```python
def fullname(self):
    return f"{self.first} {self.last}"
```

---

### Use a Class Method when:

The method needs to work with the class itself.

```python
@classmethod
def set_raise_amount(cls, amount):
    cls.raise_amount = amount
```

Or when creating an **alternative constructor**:

```python
@classmethod
def from_string(cls, emp_str):
    ...
```

---

### Use a Static Method when:

The method logically belongs to the class but doesn't need access to:

* instance data
* class data

```python
@staticmethod
def is_workday(day):
    ...
```

---

# 14. Key Concepts to Remember

### `self`

```python
self
```

→ current **instance/object**

### `cls`

```python
cls
```

→ current **class**

### `@classmethod`

```python
@classmethod
```

→ method receives `cls`

### `@staticmethod`

```python
@staticmethod
```

→ receives neither `self` nor `cls`

---

# 15. Important Code Patterns

### Instance Method

```python
def method(self):
    pass
```

### Class Method

```python
@classmethod
def method(cls):
    pass
```

### Static Method

```python
@staticmethod
def method():
    pass
```

### Alternative Constructor

```python
@classmethod
def from_string(cls, data):
    ...
    return cls(...)
```

---

# 16. Practice Questions

### Q1. What is a class method?

A method that is bound to the class and receives `cls` as its first argument.

---

### Q2. What decorator is used for class methods?

```python
@classmethod
```

---

### Q3. What does `cls` represent?

`cls` represents the class itself.

---

### Q4. What decorator is used for static methods?

```python
@staticmethod
```

---

### Q5. Does a static method receive `self` or `cls` automatically?

No.

---

### Q6. What is a major use of class methods?

Creating **alternative constructors** and modifying/accessing class-level data.

---

# 17. Summary

```text
Instance Method
      ↓
    self
      ↓
works with object/instance


Class Method
      ↓
    @classmethod
      ↓
     cls
      ↓
works with class


Static Method
      ↓
  @staticmethod
      ↓
 no self / cls
      ↓
utility/helper function
```

### Remember:

**Instance → `self`**

**Class → `cls`**

**Static → neither**
