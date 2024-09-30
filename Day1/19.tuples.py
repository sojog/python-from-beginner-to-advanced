
x = (10, 3, 5, 6, 8, 9, 10)
print(x, type(x))


a, b, *c = x
print("a=", a)
print("b=", b)
print("c=", c)

m = 11
n = 22
m, n = n, m
print("m=", m)
print("n=", n)

x = (10, 3, 5, 6, 8, 9, 10, 6565, 0)
print(x[-3])
print(len(x))
print(x[0:3])
print(x[2:5])
print(x[0:6:2])

