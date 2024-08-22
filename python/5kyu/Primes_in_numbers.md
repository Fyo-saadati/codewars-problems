# Challenge explanation


Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

```"(p1**n1)(p2**n2)...(pk**nk)"```
<br>
with the p(i) in increasing order and n(i) empty if n(i) is 1.

```Example: n = 86240 should return "(2**5)(5)(7**2)(11)"```



To see the challenge on Codewars [**click here**](https://www.codewars.com/kata/54d512e62a5e54c96200019e)
<br>
To see the my solution [**click here**](Primes_in_numbers.py)





# Solution explanation




## step 1
I have defined these 3 variables:

- ```p = 2```: This is the first prime number that we will use in our calculations. 
Over time, it will be updated to larger prime numbers.
- ```e = 0```: This variable represents the number of times the prime number has been 
multiplied by itself and is present in the input number.
- ```result``` = "": This is a string that will eventually be displayed.







## step 2
```python
while n > 1:
    if ((p % 2 != 0 and p % 3 != 0 and p % 5 != 0 and p % 7 != 0) 
    or p in (2,3,5,7)):

        while n % p == 0:
            n = n / p
            e += 1
        p += 1
        if e == 1:
            result += f"({p})"
        else:
            result += f"({p}**{e})"
        e = 0
    else:
        p += 1

```

Here, I’ve created two nested loops. Don’t worry!! It may look intimidating, 
but the conditions inside ensure that the algorithm’s performance won’t be 
negatively affected. I’ll explain what each part does below.

### First Loop Explanation:

```python
while n > 1:
    if ((p % 2 != 0 and p % 3 != 0 and p % 5 != 0 and p % 7 != 0) 
    or p in (2,3,5,7)):


        # TODO



    else:
        p += 1

```

This loop will continue running as long as the input number is greater than 1. 
As soon as the value becomes less than or equal to 1, the loop will stop.
The condition written here attempts to determine if a parameter called `p` is a 
prime number or not. To solve this problem, we need prime numbers. Instead of 
listing all prime numbers and creating an inefficient algorithm, we can use 
this condition to generate prime numbers sequentially.
As I mentioned, we need to start with a prime number. So, if a is not a prime 
number, in the else section:
As I mentioned, we need to start with a prime number. So, if `p` is not a prime 
number, in the else section:
```python
else:
    p += 1
```
`p` is incremented by 1 to eventually reach the next prime number as a increases.


## step 3

### Second Loop Explanation:
```python
while n % p == 0:
    n = n / p
    e += 1
p += 1
if e == 1:
    result += f"({p})"
else:
    result += f"({p}**{e})"
e = 0

```
The second loop will continue to run as long as the input number n, when 
divided by the prime number stored in p, has no remainder.

Why? Because we want to determine how many times each prime number appears
in the input number.

If this condition is met `while n % p == 0` these two events will occur: 
<br>
- `n = n / p`, 
<br>
- `e += 1`


In this part `n = n / p`, the input number will be divided by the prime number,
and the new value will replace the input value. By doing this, 
we systematically remove the prime factors of the input number one by one.

In this section `e += 1`, `e` is incremented by one. This number represents the exponent 
of the prime number present in the input. 
If this second loop runs three times, it means that `p` is present to the power 
of three in the input number.


### After the second loop stops:


```python

    while n%p ==0:
        n = n/p
        e +=1
    if e ==1:
        result +=f"({p})"
    if e >1:
        result +=f"({p}**{e})"
    e =0
    p +=1
    
```
After the second loop stops, immediately:`p += 1`
Why? Because we have finished working with the previous prime number, and if 
the condition of the first loop still holds, we need more prime numbers. By 
incrementing p by one, we proceed to find the next prime numbers and repeat 
the calculations.

The following two conditions are set according to the problem's requirements:

- If e, which is the exponent of the prime number, is 1, we omit it from the 
string. If e is greater than one, we include it in the string.
After either of these conditions is handled, we reset e to zero. Why? Because 
- if the condition of the first loop still holds, we need to repeat the 
calculations. Resetting e to zero prepares it for the next round of 
calculations.

## step 4
If the loop stops because the condition of the first loop is no longer met 
(i.e., n becomes less than or equal to 1), then our calculations are complete 
and we can return the result. The result will be stored in the result variable.

Our work is finished.

## Enjoyed the Code?

If you found this project helpful or interesting, please consider giving it a 
star on GitHub! ⭐

Your support motivates me to continue working on and improving this project.

[Give a Star](https://github.com/Fyo-saadati/codewars-problems) 

Thank you!