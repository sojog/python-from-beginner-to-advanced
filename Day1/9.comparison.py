euro = 4.97
usd = 4.45
amount = int(input("Insert the amount you own\n"))
currency = input("Choose currency euro/usd\n")

if amount < 2000:
    print("You are ok")
elif amount < 1000:
    print("You are okish")