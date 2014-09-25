def draw_n_squares(n):
    a = "+---"
    b = "+---+"
    c = "|   "
    d = "|   |"
    e = "\n"
    f = (a * (n - 1) + b)
    g = (e + c * (n - 1) + d + e)
    print(n * (f + g) + f)
