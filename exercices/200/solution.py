def is_prime(a):
    if a == 2:
        return True
    else:
        if a > 1:
            for i in range(3, a):
                if a % i == 0:
                    return False
                else:
                    return True
        else:
            return False
            
