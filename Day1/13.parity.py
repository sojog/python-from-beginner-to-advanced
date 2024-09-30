n = int(input("Insert the number\n"))

if n % 2 == 0:
    result = True
else:
    result = False
print(f"Number is even: {result}")

print("Even") if n % 2 == 0 else print("Odd")

print(f"Number is even: {n % 2 == 0}")
