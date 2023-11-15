def uppercase_operator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@uppercase_operator
def say_hi():
    return 'hello there'

print(say_hi())
