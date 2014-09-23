alph = ("abcdefghijklnmopqrstuvwxyz")
a = len(alph)
c = 0
for i in alph:
    while c < a:
        print(i + alph[c])
        c = c + 1
    c = 0
