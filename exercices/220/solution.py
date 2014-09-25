import is_prime
c = []
d = []
for i in range(10000, 10050):
    if is_prime.is_prime(i) is True:
        c.append(str(i))
print(", ".join(c))
