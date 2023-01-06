def highly_divisible_triangular_number(num_of_factors):
    def get_factors(num):
        factors = []
        for i in range(1, int(num ** 0.5) + 1):
            if not i in factors:
                if num % i == 0:
                    factors.append(i)
                    if i != num ** 0.5:
                        factors.append(int(num / i))
        return factors

    factors = []
    counter = 1
    current_val = 0

    while not len(factors) > num_of_factors:
        current_val += counter
        factors = get_factors(current_val)
        counter += 1

    return current_val

print(highly_divisible_triangular_number(500))



