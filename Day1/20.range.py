

x = list(range(3, 10))
print(x)


for i in range(9, 3, -1):
    print(i)



cars = ["Dacia", "BMW", "VW", "Toyota", "Mazda", "Mercedes"]
for c in cars:
    print(c)

for i in range(len(cars)):
    print(i, cars[i])

for index, value in enumerate(cars):
    print(index, value)