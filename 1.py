def multiples_of_3_or_5(max):
    counter = 0
    for i in range(1,max):
        if i % 3 == 0 or i % 5 == 0:
            counter += i
    return counter

result = multiples_of_3_or_5(1000)
print(result)