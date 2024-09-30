# %%
print("good" == "great" or 67 != 76)

# %%
print(False or True)

# %%
x = "Hello"
print(bool(x))
if x:
    print("True")
    
    # %%

name = ["robert"]
winner = ["robert"]
same_address = winner
print(name == winner)
print(name is winner)
print(same_address is winner)

# %%
name = "robert"
print(name == "Robert")

# %%
_T = "1234___"
my_var_ = "1234?"
my#var = 0.0

# %%

a = 10
b = 0
print ( a/b ) if (b == 0 ) else print ( a )

# %%

if 1:
    print("always")
else:
    print("never")
    
    # %%

a = (3, 2, 3, 4)
print(a)
print("lenght:",len(a))
print(type(a))

# %%
a = tuple()
print(a) 

# %%
b = list()
print(b)

# %%
c = dict()
print(c)

# %%
if False:
    print("Real")
elif True:
    print("Milan")
elif True:
    print("Liverpool")
else:
    print("Bayern")