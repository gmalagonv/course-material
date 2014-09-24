import is_prime
c = 0
for i in range(1, 1000):
    if is_prime.is_prime(i) is True:
        c = c + i
print(c)
