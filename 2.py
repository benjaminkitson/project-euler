def even_fibonnaci_numbers():
    fibonacci = [1,2]
    counter = 2

    is_over = False

    while not is_over:
        if fibonacci[-1] + fibonacci[-2] < 4000000:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
            if fibonacci[-1] % 2 == 0:
                counter += fibonacci[-1]
        else:
            is_over = True
    
    return counter

result = even_fibonnaci_numbers()
print(result)
