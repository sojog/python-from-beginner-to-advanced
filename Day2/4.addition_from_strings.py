a = "1,2,3,7,8"
b = "4,5,6"

c = "5,7,9,7,8" # desired outcome

a = a.split(",")
print(a)
a = [int(i) for i in a]
print(a)

b = b.split(",")
print(b)
b = [int(i) for i in b]
print(b)


min_len = min(len(a), len(b))
longer_list = a if len(a) > len(b) else b
c = [ a[i] + b[i] for i in range(min_len)]
c += longer_list[min_len:]
print(c)

# V1
new_str = ""
for i in c:
    if new_str:
        new_str += ","
    new_str += str(i)
print(new_str)

# V2 
print(",".join([str(i) for i in c]))
