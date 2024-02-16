def sum_of_multiples(limit):
    total = 0
    for num in range(limit):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total

limit = 1000
result = sum_of_multiples(limit)
print("The sum of all the multiples of 3 or 5 below", limit, "is:", result)

