# def square(x):
#     return x ** 2

# ## Removing the Parenthesis and treating f as a function
# f = square

# print(f(5))

# print(square)

def square(x):
    return x ** 2

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])

print(squares)

def cube(x):
    return x ** 3