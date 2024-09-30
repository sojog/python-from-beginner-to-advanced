
def another_function():
    return 300


def decorator(func_param):
    print("Decorator is called")
    return func_param

@decorator
def func():
    return 10

@decorator
def second_deco_func():
    return 20

print(func())
print(second_deco_func())