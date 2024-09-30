"""Create a program in which the user will insert an integer amount.The program must calculate and display the corresponding number of banknotes, where the program defines the banknotes with the values: 10, 5, 2 and 1."""

# 10, 5, 2 and 1
amount = 2538
print(f"amount={amount}")

tens = amount // 10
print(f"tens:{tens}") 

rest_after_tens = amount % 10

fives = rest_after_tens // 5
print(f"fives:{fives}")

rest_after_fives = rest_after_tens % 5

twos = rest_after_fives // 2
print(f"twos: {twos}")

rest_after_twos = rest_after_fives % 2
ones = rest_after_twos // 1
print(f"ones: {ones}")