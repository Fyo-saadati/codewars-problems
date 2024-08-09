from math import sqrt


def sum_of_squares(n):
    input_ = n
    if sqrt(n) % 1 == 0:
        return 1

    while n % 4 == 0:
        n = n / 4

    if n % 8 == 7:
        return 4

    largest_square = int(sqrt(input_))
    while largest_square >= 0:
        t = input_ - (largest_square**2)
        if t + largest_square**2 == input_ and sqrt(t) % 1 == 0:
            return 2
        else:
            largest_square -= 1
    return 3
