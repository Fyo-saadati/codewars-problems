"""The task is simply stated. Given an integer n (3 < n < 109), 
find the length of the smallest list of perfect squares which 
add up to n. Come up with the best algorithm you can; you'll need it!

Examples:

sum_of_squares(17) = 2
17 = 16 + 1 (16 and 1 are perfect squares).
sum_of_squares(15) = 4
15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three perfect squares.
sum_of_squares(16) = 1
16 itself is a perfect square.
Time constraints:

5 easy (sample) test cases: n < 20

5 harder test cases: 1000 < n < 15000

5 maximally hard test cases: 5e8 < n < 1e9

15 random maximally hard test cases: 1e8 < n < 1e9"""

from math import sqrt


def sum_of_squares(n):
    input_ = n
    if sqrt(n) % 1 == 0:
        return 1

    while n % 4 == 0:
        n = n / 4

    if n % 8 == 7:
        return 4

    if sqrt(n / 2) % 1 == 0:
        return 2

    largest_squre = int(sqrt(input_))
    while largest_squre >= 0:
        t = input_ - (largest_squre**2)
        if t + largest_squre**2 == input_ and sqrt(t) % 1 == 0:
            return 2
        else:
            largest_squre -= 1
    return 3
