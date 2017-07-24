def is_prime(number):
    for i in range(number - 1, 2, -1):
        if number % i == 0:
            return False
        else:
            return True

if is_prime(11):
    print('YES')