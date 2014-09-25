al = ("abcdefghijklmnopqrstuvwxyz")
al2 = al.upper()
al3 = al+al2
dic = {}
for i in al3:
    dic[i] = 0
f = open('words', 'r')
for line in f:
    for h in line:
        if h in dic:
            dic[h] = dic[h] + 1
for p in dic:
    if dic[p] != 0:
        a = dic[p]
        print(p + ":", a)
