"""Create a program in which the user will insert an integer amount.The program must calculate and display the corresponding number of banknotes, where the program defines the banknotes with the values: 10, 5, 2 and 1."""

def extract_banknotes(amount, banknotes):
    d = {}
    for i in banknotes:
        print(f"{i}:{amount // i}")
        d[f"{i}"] = amount // i
        amount = amount % i
    return d

amount = 137
banknotes = [50, 20, 10, 1]
result = extract_banknotes(amount, banknotes)
print("Result:", result)

print(result["50"])
