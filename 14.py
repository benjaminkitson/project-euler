def longest_collatz_sequence(max_val):
    def get_sequence(num):
        sequence = [num]
        while not num == 1:
            if num % 2 == 0:
                num = num / 2
            else:
                num = (3 * num) + 1
            sequence.append(num)
        return sequence

    result = None
    max_length = 0

    for i in range(1, max_val + 1):
        sequence = get_sequence(i)
        if len(sequence) > max_length:
            max_length = len(sequence)
            result = i

    return result

print(longest_collatz_sequence(1000000))
