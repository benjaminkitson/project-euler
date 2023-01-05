def special_pythagorean_triplet():

    a = 1
    b = 2

    def get_c():
        return 1000 - (a + b)

    c = get_c()

    def is_valid():
        return a ** 2 + b ** 2 == c ** 2

    while not is_valid():
        while b < c:
            b += 1
            c = get_c()
            if is_valid():
                return a * b * c
        a += 1
        b = a + 1
        c = 1000 - (a + b)

print(special_pythagorean_triplet())

