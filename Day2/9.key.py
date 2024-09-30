
l = ["Bucharest", "Berlin", "Belgrade","Beirut", "Amsterdam", "Barcelona"]
print(sorted(l))
print(sorted(l, key=len))

print(min(l))
print(min(l, key=len))
print(max(l, key=len))