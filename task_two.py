fractional_numbers = [10.4, 16.9, 10.4, 4.0, 10.6, 17.6, 19.6, 10.1, 12.0, 16.3]
fractional_numbers.sort(key = float)

def binary_search(array: list, x: int|float):
    left = 0
    right = len(array) - 1
    EPSILON = 1e-12
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        middle = left + (right - left) // 2

        if abs(array[middle] - x) < EPSILON:
            upper_bound = array[middle]
            return (iterations, upper_bound)
        elif array[middle] < x:
            left = middle + 1
        else:
            upper_bound = array[middle]
            right = middle - 1
    
    return (iterations, upper_bound)

result = binary_search(fractional_numbers, 17)
print(f'Iterations {result[0]}, Upper bound {result[1]}')

# Note: Example of search on fractional numbers is taken here https://medium.com/@sanjaysoni_48818/binary-search-for-integer-float-range-44d34e688874
