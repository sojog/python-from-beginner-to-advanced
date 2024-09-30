
def func():
    return (10, 20)

result = func()
print(result, type(result))


a = result[0]
b = result[1]
print("a=", a)
print("b=", b)

a = result
print("a=", a)



print(func)
print(func())

x = func
print(x)
print(x())


text = str
print(text(300))

# Passing a function as a parameter
def convert(value, func):
    return func(value)

print(convert(20.4, int))



