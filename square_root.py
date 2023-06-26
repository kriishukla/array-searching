def square_root_binary_search(number, epsilon=0.01):
    if number < 0:
        raise ValueError("Square root undefined for negative numbers.")

    low = 0.0
    high = max(number, 1.0)

    while high - low > epsilon:
        mid = (low + high) / 2
        square = mid * mid

        if square == number:
            return mid
        elif square < number:
            low = mid
        else:
            high = mid

    return (low + high) / 2


number = 17
result = square_root_binary_search(number)
print(result)
