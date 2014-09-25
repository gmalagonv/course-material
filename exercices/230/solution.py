import is_prime
a = 100000001
while is_prime.is_prime(a) is False:
    a = a + 1
else:
    print(a)
    