a = [1, 2, 3, 7, 8]
b = [4, 5, 6]

## Classic solution
c = []
min_len = min(len(a), len(b))
for i in range(min_len):
    c.append(a[i] + b[i])
print(c)

longer_list = a if len(a) > len(b) else b
print(longer_list)
print(longer_list[min_len:])

c += longer_list[min_len:]
print(c)