## Challenge explanation

The task is simply stated. Given an integer n (3 < n < 1e9),
find the length of the smallest list of perfect squares which
add up to n. Come up with the best algorithm you can; you'll need it!

Examples:

sum_of_squares(17) = 2
17 = 16 + 1 (16 and 1 are perfect squares).
sum_of_squares(15) = 4
15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three 
perfect squares.
sum_of_squares(16) = 1
16 itself is a perfect square.
Time constraints:

5 easy (sample) test cases: n < 20

5 harder test cases: 1000 < n < 15000

5 maximally hard test cases: 5e8 < n < 1e9

15 random maximally hard test cases: 1e8 < n < 1e9

To see the challenge on Codewars [**click here**](sums_of_perfect_squares.py)
<br>
To see the my solution [**click here**](sums_of_perfect_squares.py)


## Solution
for check my solution please [**click here**](https://www.codewars.com/kata/5a3af5b1ee1aaeabfe000084)


# Challenge explanation
According to Lagrange's theorem, we know that all positive numbers can be 
expressed as a sum of up to 4 perfect squares. Gauss's theorem helps us ensure 
that a given number is definitely made up of 4 perfect squares. Remember, 
I will explain how I used this in my solution.


### step 1
I removed all numbers that are already perfect squares using this method:

```python
if sqrt(n) % 1 == 0:
        return 1
```
By this method, if the number is a perfect square, we immediately return 1. 
This helps us avoid unnecessary loops.






### step 2
I used Gauss's theorem on four squares to identify numbers that are composed 
solely of four perfect squares. Below is an explanation of the theorem:


### Gauss's Theorem on Four Squares:

This theorem states that if a number is of the form

$n = 4^a \times (8b + 7)$
<br>
For further study on this topic, click on this [**link**](https://askubuntu.com/questions/833448/how-can-i-update-visual-studio-code-on-ubuntu).
<p>
which means that after repeatedly dividing the number by 4, if you end up with 
a remainder of 7 when divided by 8, then this number can never be expressed as 
the sum of three squares. In other words, a number of this form must be 
expressible as the sum of four squares.
</p>


### How to verify this theorem:

#### Repeated Division by 4: 
Divide the given number repeatedly by 4 until you 
get a number that is no longer divisible by 4 (or more precisely, 
until the remainder after division by 4 is no longer zero).

#### Remainder when Divided by 8: 
Now, divide the resulting number by 8. If the remainder of this division is 7, 
then the original number must generally be expressible as a sum of four squares.


In the following code snippet, we repeatedly divide the given number by four 
until we obtain the final remainder.

```python
while n % 4 == 0:
    n = n / 4
```


In the following code snippet, we check whether the final remainder,
 when divided by eight, gives a remainder of 7. If the remainder of this 
 division is 7, then the number in question is definitely composed of four 
 perfect squares.


```python
if n % 8 == 7:
return 4
```

> So far, we can definitely identify numbers that are perfect squares 
themselves and numbers that are composed of four perfect squares.


### step 3

#### what is this : ```input_ = n``` ?
<p>I defined this variable to have a copy of the input number, 
because in previous steps the input number had been modified.


In my opinion, identifying numbers that are composed of 2 perfect squares is 
simpler than identifying those composed of 3 perfect squares. Therefore, for
this task, the simplest approach that came to mind was to take the square root 
of the input number. This gives us the square of the first perfect square that 
might be present in the number. Then, I subtract this perfect square from the 
input. If the remainder is also a perfect square, then the input number is 
definitely the sum of two perfect squares.

If neither part is a perfect square during the loop, the process continues by 
decrementing the largest square by one unit. This process continues until the 
combination is confirmed.</p>




This part is responsible for identifying numbers that are composed of two perfect squares.

```python
largest_square = int(sqrt(input_))
while largest_square >= 0:
    t = input_ - (largest_square**2)
    if t + largest_square**2 == input_ and sqrt(t) % 1 == 0:
        return 2
    else:
        largest_square -= 1
```

### step 4

After three steps, numbers composed of 1, 2, and 4 perfect squares have been 
identified. In the fourth step, without any further calculations, it is certain 
that the input number is composed of 3 perfect squares.