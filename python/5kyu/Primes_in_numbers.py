def prime_factors(n):
    p = 2
    e = 0
    result = ""
    while n > 1:
        if (p % 2 != 0 and p % 3 != 0 and p % 5 != 0 and p % 7 != 0) or p in (
            2,
            3,
            5,
            7,
        ):

            while n % p == 0:
                n = n / p
                e += 1
            if e == 1:
                result += f"({p})"
            if e > 1:
                result += f"({p}**{e})"
            e = 0
            p += 1
        else:
            p += 1

    return result
