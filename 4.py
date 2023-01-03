def largest_palindrome_product():
    def string_reverse(str):
        arr = list(str)
        arr.reverse()
        return "".join(arr)

    def is_palindrome(str):
        return str == string_reverse(str)

    max = 0

    for x in range(999, 910, -1):
        for y in range(x, 910, -1):
            if is_palindrome(str(x*y)) and (x*y > max):
                max = x*y

    return max

print(largest_palindrome_product())

    
    
