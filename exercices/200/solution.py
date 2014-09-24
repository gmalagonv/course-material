def is_prime(a):
    if a == 2 or a == 3:
        return True
    else:
        if a > 1:
            for i in range(2, a):
                if a % i == 0:
                    return False
                else:
                    return True
        else:
            return False
