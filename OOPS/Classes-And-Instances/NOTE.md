# OOP Concepts

## Why Should We Use Classes?

Classes allow us to **logically group related data and functions** together.

They make our code:

* Easier to organize
* Easier to reuse
* Easier to maintain
* Easier to extend when the application grows

For example, an `Employee` class can contain both the employee's **data** (name, salary, email) and **functions** (such as displaying the full name).

---

## Methods

A **method** is a function that is associated with a class.

Example:

```python
class Employee:
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
```

Here, `fullname()` is a method of the `Employee` class.

---

## Instance Variables

An **instance variable** contains data that is **unique to each instance (object)** of a class.

Example:

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
```

Here:

* `self.first` → unique first name for each employee
* `self.last` → unique last name for each employee
* `self.pay` → unique salary for each employee

So:

```python
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)
```

`emp_1` and `emp_2` have different values for their instance variables.

---

# Constructor — `__init__()`

The `__init__()` method is commonly used as the **constructor** of a Python class.

It runs automatically whenever we create a new object.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
```

When we create:

```python
emp_1 = Employee('John', 'Doe', 50000)
```

Python automatically calls:

```python
__init__(emp_1, 'John', 'Doe', 50000)
```

The `self` parameter refers to the **current instance/object**.

---

# The `self` Parameter

## Common Mistake

When creating an instance method, it is easy to forget the `self` parameter.

❌ Incorrect:

```python
class Employee:
    def fullname():
        return '{} {}'.format(self.first, self.last)
```

The method does not accept any parameter, but Python automatically passes the instance when calling it.

Therefore:

```python
emp_1.fullname()
```

is internally treated approximately like:

```python
Employee.fullname(emp_1)
```

This causes:

```text
TypeError: Employee.fullname() takes 0 positional arguments but 1 was given
```

---

## Correct Method

We need to include `self`:

```python
class Employee:
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
```

Now:

```python
emp_1.fullname()
```

works correctly.

---

# Complete Example

```python
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # Method to display the full name
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())
```

### Output

```text
John.Doe@company.com
Jane.Smith@company.com
John Doe
Jane Smith
```

---

# Two Ways to Call an Instance Method

Both of these produce the same result:

### 1. Using the object

```python
print(emp_1.fullname())
```

### 2. Using the class

```python
print(Employee.fullname(emp_1))
```

The first approach is the **normal and preferred way**.

Python automatically passes `emp_1` as the `self` argument:

```python
emp_1.fullname()
```

is effectively:

```python
Employee.fullname(emp_1)
```

---

# Key Takeaways

* A **class** is a blueprint for creating objects.
* An **object/instance** is a specific instance of a class.
* A **method** is a function associated with a class.
* `__init__()` initializes an object when it is created.
* **Instance variables** contain data unique to each object.
* `self` refers to the current instance.
* Python automatically passes the instance to an instance method.
* Therefore, instance methods must include `self` as their first parameter.

### Remember

> `emp_1.fullname()` → Python automatically passes `emp_1` as `self`.
