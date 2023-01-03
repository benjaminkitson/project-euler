def smallest_multiple():
    counter = 190
    success = False
    while not success:
        is_valid = True
        for i in range(20, 10, -1):
            if counter % i != 0:
                is_valid = False
                break
        if is_valid:
            break
        counter += 190
    return counter

print(smallest_multiple())
