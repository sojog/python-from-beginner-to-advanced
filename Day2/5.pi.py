

text = "dar, e bine a relua lucrurile de foarte multe ori"
print(text.split(","))

parts = text.split(",")

pi = ""
for p in parts:
    words =  p.split()
    print(words)

    lengths = [ str(len(i)) for i in words]
    print(lengths)

    joined = "".join(lengths)
    if pi:
        pi = pi + ","
    pi = pi + joined

print(pi)







