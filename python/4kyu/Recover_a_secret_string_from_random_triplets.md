## Challenge explanation

There is a secret string which is unknown to you. 
Given a collection of random triplets from the string, 
recover the original string.

A triplet here is defined as a sequence of three letters such that each letter 
occurs somewhere before the next in the given string. 
"whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more 
than once in the secret string.

You can assume nothing about the triplets given to you other than that they 
are valid triplets and that they contain sufficient information to deduce 
the original string. In particular, this means that the secret string will 
never contain letters that do not occur in one of the triplets given to you.



To see the challenge on Codewars [**click here**](https://www.codewars.com/kata/53f40dff5f9d31b813000774)
<br>
To see the my solution [**click here**](Recover_a_secret_string_from_random_triplets.py)






# Solution explanation
At first glance, this problem seems very difficult. But when we pay a little 
attention, we realize that this problem is not that difficult and can be easily 
solved, and we can handle it.
If we find the first character and then delete it from the list, 
the next character moves to the first position, and we can repeat this with it
 until all characters are found. Now let's see what each line of my algorithm 
 meansAccording to Lagrange's theorem, we know that all positive numbers can be 
expressed as a sum of up to 4 perfect squares. Gauss's theorem helps us ensure 
that a given number is definitely made up of 4 perfect squares. Remember, 
I will explain how I used this in my solution.


### step 1
A string variable, ```result_str```, is declared to store the computed output. This variable will be returned as the function's result.

```python
result_str = ""
```

We eliminate duplicate characters this way and store only the unique 
characters in the variable `ch_set`

```python
ch_set = list(set("".join(["".join(ls) for ls in triplets])))
```

`Note:`  To understand the solution correctly, I should start explaining 
from the second loop, so for now, we won’t focus on the while loop.

### step 2
For the second step, we need to define a loop and iterate over the characters 
in the set we created and stored in ch_set.

```python
for ch in ch_set:
```



### step 3
Now, we define a flag and set its value to True. We create another loop inside 
the first loop and iterate over the sublists in triplets. This way, we can 
check if the character exists in the target list and if its index is equal to 
zero or not. If it isn’t equal to zero, it means we have a character that 
exists in the lists but doesn’t hold the first position, so we set the flag to 
False. The program then stops and breaks out of the loop, returns to the first 
loop, and moves on to the next character.

```python
 flag = True
for ls in triplets:
        if ch in ls and ls.index(ch) != 0:
                flag = False
                break
```



### step 4
If the condition we defined in the previous step isn’t met, the flag won’t 
become False. What does this mean? It means the character only exists in the 
first position, and this is the character we need to select. So, we check if 
the flag is True. Then, we iterate over triplets again, remove the character 
we last checked from all the lists in triplets, and check if we haven’t already 
added the character to the result variable. If not, we add it.


```python
if flag:
        for ls in triplets:
                if ch in ls:
                if ch not in result_str:
                        result_str += ch
                ls.remove(ch)
```


### step 5
Alright, now it's time to go over the while loop.

So far, we’ve done everything correctly, but our work isn’t done yet. If you 
pay attention, you’ll notice that when the loop iterates over ch_set once, it 
identifies a few characters and processes them correctly. However, in the 
first pass of checking, some characters may not be in the first position, 
so they get skipped. Now that our first loop has finished, those characters 
have moved to the first position, but the loop is over, and no more actions 
are happening.

Do you see the necessity of using a while loop now? The while loop allows us 
to repeat this process as needed until all characters are identified.

So, what should the stopping condition of the while loop be? Remember that in 
the previous step, we removed the identified characters from the lists. So, 
we can conclude that eventually, some lists will lose all their characters and 
become empty.

When should we stop? When all the lists in triplets are empty. If we remove 
the empty lists, and the length of triplets is zero, it means there’s nothing 
left to check, and our task is complete, so we can stop the loop!

Thus, our stopping condition is when the length of triplets is zero.

```python
while len(triplets) > 0:
```
And with the following line, we remove the emptied lists from triplets 
and override the triplets variable:


```python 
triplets = list(filter(None, triplets))
```


and we can return `result` as an answer 



## Enjoyed the Code?

If you found this project helpful or interesting, please consider giving it a 
star on GitHub! ⭐

Your support motivates me to continue working on and improving this project.

[Give a Star](https://github.com/Fyo-saadati/codewars-problems) 

Thank you!