def sum_square_difference():
    sum_squares = 0
    square_sum = 0
    for i in range(1, 101):
        sum_squares += i ** 2
        square_sum += i

    square_sum **= 2

    return(abs(sum_squares - square_sum))

print(sum_square_difference())
