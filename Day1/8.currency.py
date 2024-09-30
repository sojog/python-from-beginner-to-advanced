euro = 4.97
usd = 4.45
amount = int(input("Insert the amount you own\n"))
currency = input("Choose currency euro/usd\n")

if currency == "euro":
    ron = amount * euro
elif currency == "usd":
    ron = amount * usd
else:
    ron = "undefined"

print("The sum is :", ron, "RON")
print("The sum is :" +  str(ron) + "RON")
print(f"The sum is : {ron} RON")
