alph = ("abcdefghijklmnopqrstuvwxyz")
a = len(alph)
c = 0
lista = []
for i in alph:
    while c < a:
        d = (i + alph[c])
        e = (alph[c] + i)
        if d in lista:
            c = c + 1
        else:
            print(d)
            c = c + 1
        lista.append(d)
        if d != e:
            lista.append(e)
    c = 0
