n = input("Insert the number\n")

while not n.isnumeric():
    print("It NOT is numeric")
    n = input("Insert the number\n")

n = int(n)

print(f"Insert value is even:{ n % 2 == 0}")
print(f"Insert value is even:{ bool(n % 2) }")
print(f"Insert value is even:{ not bool(n % 2) }")
print(f"Insert value is even:{ not (n % 2) }")


