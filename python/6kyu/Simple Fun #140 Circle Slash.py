"""DESCRIPTION:
Task
Suppose there are n people standing in a circle and they are numbered 1 through n in order.

Person 1 starts off with a sword and kills person 2. He then passes the sword to the next 
person still standing, in this case person 3. Person 3 then uses the sword to kill person 4, 
and passes it to person 5. This pattern continues around and around the circle until just 
one person remains.

What is the number of this person?

Example:
For n = 5, the result should be 3.

 1 kills 2, passes to 3. 3 kills 4, passes to 5. 5 kills 1, passes to 3. 3 kills 5 and wins.

Input/Output
[input] integer n
The number of people. 1 through n standing in a circle.

1 <= n <= 1e9

[output] an integer
The index of the last person standing."""


#solution:

def circle_slash(n):
    num =2
    dict1={1:1, 2:1, 3:3, 4:1}
    while  2**num <n:   
        num +=1
    if n <=4:
        return dict1[n]
    if n == 2**num :
        return 1
    return (n-(2**num)) + n+1
