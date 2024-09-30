"""Two lists are given with members 1,2,3 and 4,5,6.
A third list must be created that will contain the sum of the members of the two existing lists (5, 7 and 9)."""

a = [1, 2, 3]
b = [4, 5, 6]

## Classic solution
c = []
for i in range(len(b)):
    c.append(a[i] + b[i])
print(c)

## List comprehetion
c = [a[i] + b[i] for i in range(len(b))]
print(c)