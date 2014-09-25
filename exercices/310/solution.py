f = open('words', 'r')
c = 0
for line in f:
    for h in line:
        if h == "e":
            c = c + 1
print(c)
