def largest_prime_factor(val):
    prime_factors = []
    i = 1

    def test_five_three(num):
        return num % 3 != 0 and num % 5 != 0

    def repeat_divide(num, divisor):
        return_val = num
        is_divisible = num % divisor == 0
        if is_divisible:
            prime_factors.append(divisor)
            return_val /= divisor
            repeat_divide(return_val, divisor)
        return return_val

    for i in [3,5]:
        val = repeat_divide(val, i)

    while len(prime_factors) == 0 or prime_factors[-1] < val:
        minus = (6 * i) - 1
        if test_five_three(minus):
            val = repeat_divide(val, minus)
        plus = (6 * i) + 1
        if test_five_three(plus):
            val = repeat_divide(val, plus)
        i += 1

    return prime_factors[-1]

print(largest_prime_factor(600851475143))




    