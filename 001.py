def multiples_of_3_and_5(start, end):
    sum = 0

    for i in range(start, end):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    print(sum)

multiples_of_3_and_5(0, 1000)
