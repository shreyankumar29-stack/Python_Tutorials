# First-Class Functions in Python

This repository contains my notes and practice code while learning **First-Class Functions in Python** from **Corey Schafer**.

First-class functions are an important Python concept because functions can be treated as **objects**. Understanding this concept makes it easier to learn **higher-order functions, closures, and decorators**.

---

## 📚 Source

* **Instructor:** Corey Schafer
* **Topic:** First-Class Functions
* **Language:** Python

---

## 🎯 Learning Objectives

By completing this topic, I aim to understand:

* What first-class functions are
* Why functions are objects in Python
* Assigning functions to variables
* Passing functions as arguments
* Returning functions from other functions
* Storing functions in data structures
* The difference between a function and a function call
* How first-class functions lead to higher-order functions
* The connection between first-class functions and decorators

---

## 🧠 What Are First-Class Functions?

In Python, functions are **first-class objects**.

This means a function can be treated like other Python objects such as:

* Integers
* Strings
* Lists
* Dictionaries
* Classes

A function can be:

1. Assigned to a variable
2. Passed as an argument
3. Returned from another function
4. Stored in a list, tuple, or dictionary

---

## 1. Assigning a Function to a Variable

```python
def square(x):
    return x * x


my_function = square

print(my_function(5))
```

### Output

```text
25
```

Here:

```python
my_function = square
```

does not execute `square`.

Instead, `my_function` refers to the same function object.

### Important

```python
square
```

refers to the function itself.

```python
square(5)
```

calls the function and returns its result.

---

## 2. Passing a Function as an Argument

Functions can be passed to other functions.

```python
def square(x):
    return x * x


def execute_function(func, value):
    return func(value)


result = execute_function(square, 5)

print(result)
```

### Output

```text
25
```

Here, `square` is passed as an argument to `execute_function()`.

```python
execute_function(square, 5)
```

The receiving function can then call it:

```python
func(value)
```

---

## 3. Storing Functions in a List

Since functions are objects, they can also be stored inside data structures.

```python
def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


operations = [add, multiply]

print(operations[0](10, 5))
print(operations[1](10, 5))
```

### Output

```text
15
50
```

The list contains references to the functions.

---

## 4. Returning a Function

A function can also return another function.

```python
def outer():
    def inner():
        print("Hello from inner function")

    return inner


my_function = outer()

my_function()
```

### Output

```text
Hello from inner function
```

Here, `outer()` returns the `inner` function.

This concept becomes especially important when learning **closures** and **decorators**.

---

## 5. Function vs Function Call

One of the most important things to understand is the difference between:

```python
square
```

and:

```python
square()
```

### Function object

```python
x = square
```

`x` now refers to the function.

### Function call

```python
x = square(5)
```

The function is executed and its returned value is stored in `x`.

---

## 🔄 How First-Class Functions Connect to Other Concepts

The concepts build upon each other:

```text
First-Class Functions
        ↓
Functions as Objects
        ↓
Passing Functions
        ↓
Returning Functions
        ↓
Higher-Order Functions
        ↓
Closures
        ↓
Decorators
```

Understanding first-class functions is therefore an important step toward understanding Python decorators.

---

## 📝 Key Takeaways

* Python functions are objects.
* Functions can be assigned to variables.
* Functions can be passed as arguments.
* Functions can be returned from other functions.
* Functions can be stored inside lists, tuples, and dictionaries.
* `function` refers to the function object.
* `function()` executes the function.
* First-class functions are the foundation for concepts such as higher-order functions, closures, and decorators.

---

## 💻 Practice

The following examples are included in this topic:

* Assigning functions to variables
* Passing functions as arguments
* Returning functions
* Storing functions in lists
* Understanding function references
* Understanding function calls

---

## 📂 Suggested Folder Structure

```text
first-class-functions/
│
├── README.md
│
├── first_class_functions.py
│
└── practice/
    ├── functions_as_objects.py
    ├── passing_functions.py
    ├── returning_functions.py
    └── function_list.py
```

## 🚀 Next Topics

After completing First-Class Functions, the recommended progression is:

1. Higher-Order Functions
2. Closures
3. Decorators
4. `*args` and `**kwargs`
5. Lambda Functions
6. `map()`, `filter()`, and `reduce()`

---

## 📌 Notes

These notes and practice programs are part of my Python learning journey while following Corey Schafer's tutorials.

The purpose of this repository is to understand the concepts through **hands-on practice**, rather than simply copying the tutorial code.
