alph = ("abcdefghijklnmopqrstuvwxyz")
a = len(alph)
c = 0
for i in alph:
    while c < a:
        if i == alph[c]:
            c = c+1
        else:
            print(i + alph[c])
            c = c + 1
    c = 0
