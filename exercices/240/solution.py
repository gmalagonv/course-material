d = []
a = [1, 2, 3]
b = 3
for i in range(0, 7):
    c = a[b - 1] + a[b - 2]
    a.append(c)
    b = b + 1
for i in a:
    d.append(str(i))
print(", ".join(d) + ".")
