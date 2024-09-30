text = "dar, e bine a relua lucrurile de foarte multe ori"
print(text.split(","))

parts = text.split(",")

numbers = []
for p in parts:
    numbers.append("".join([str(len(i)) for i in p.split()]))

print(numbers)
print(",".join(numbers))
    
# https://dontpad.com/michelin1