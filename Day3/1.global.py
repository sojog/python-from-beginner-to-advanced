# global
x = 10

def func():
    global x
    x = 2
    print("local:", x)

func()
print("globalx:", x)


