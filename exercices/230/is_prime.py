def is_prime(a):
    if a % 2 == 0:
        return False
    else:
        if a > 1:
            b = 2
            while b < a:
                if a % b == 0:
                    return False
                b = b + 1
            else:
                return True
        else:
            return False
