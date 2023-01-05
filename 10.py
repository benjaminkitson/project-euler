def summation_of_primes(): 
    counter = 0

    primes = [2]

    def is_prime(num):
        for n in primes:
            if n > num ** 0.5:
                return True
            if num % n == 0:
                return False

    for i in range(2, 2000001):
        if is_prime(i):
            primes.append(i)
            counter += i

    return counter

print(summation_of_primes())