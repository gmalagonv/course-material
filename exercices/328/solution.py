def mul(a):
    b = len(a)
    c = 0
    d = 1
    while c < b:
        d = d * a[c]
        c = c + 1
    return(d)
