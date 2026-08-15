def outer_func(msg):
    message = msg

    def inner_func():
        print(message) # free variable inside inner function

    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello!')

hi_func()
hello_func()