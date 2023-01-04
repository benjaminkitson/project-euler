def _10001st_prime():
    primes = [2,3,5,7]
    i = 2

    def is_prime(num):
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True

    while len(primes) < 10001:
        if is_prime((6 * i) - 1):
            primes.append((6 * i) - 1)
        if len(primes) == 10001:
            break
        if is_prime((6 * i) + 1):
            primes.append((6 * i) + 1)
        i += 1

    return primes[10000]

print(_10001st_prime())