resp = []
trec = []
dc = []
import mul
f = open('digit', 'r')
for line in f:
    a = line
b = len(a)
e = 0
while e < (b - 12):
    f = e+13
    c = a[e:f]
    for i in c:
        trec.append(int(i))
    k = (mul.mul(trec))
    resp.append(k)
    e = e + 1
    pp = trec
    dc.append(pp)
    trec = []
print(max(resp))
