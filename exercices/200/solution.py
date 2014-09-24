def is_prime(a):
    if a == 2 or a == 3:
        print("True")
    else:
        if a > 1:
            b = 2
            while b < a:
                if a % b == 0:
                    print("False")
                    break
                b = b + 1
            else:
                print("True")
        else:
            print("False")
