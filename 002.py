def fibonacci_sequence():
    fibonacci = [1, 1]

    even_values_sum = 0

    for i in range(0, 100000000):
        next_fibonacci_number = fibonacci[i] + fibonacci[i + 1]

        if next_fibonacci_number < 4000000:
            fibonacci.append(next_fibonacci_number)
            if next_fibonacci_number % 2 == 0:
                even_values_sum += next_fibonacci_number
        else:
            break

    print(even_values_sum)

fibonacci_sequence()
