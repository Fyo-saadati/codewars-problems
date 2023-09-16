"""Task
If possible, divide the integers 1,2,…,n into two sets of equal sum.

Input
A positive integer n <= 1,000,000.

Output
If it's not possible, return [ ] (Javascript and Python) or 
( ) (Python) or None (Scala). If it's possible, return two disjoint sets.
Each integer from 1 to n must be in one of them. The integers in the first 
set must sum up to the same value as the integers in the second set. The sets 
can be returned in a tuple, list, or array, depending on language.

Examples:
For n = 8, valid answers include:

[1, 3, 6, 8], [2, 4, 5, 7] (or [[1, 3, 6, 8], [2, 4, 5, 7] ])

[8, 1, 3, 2, 4], [5, 7, 6]

[7, 8, 3], [6, 1, 5, 4, 2], and others.

For n = 9 it is not possible. For example, try [6, 8, 9] and [1, 2, 3, 4, 5, 7], 
but the first sums to 23 and the second to 22. No other sets work either."""

#----------answer -- >:
def create_two_sets_of_equal_sum(n): 
    list1=[]
    if (index:= sum([num for num in range(1,n+1)])) %2!=0:
        return []
    index = index//2
    patt= [i for i in range(1, n+1)][::-1]
    half= 0
    for i, num in enumerate(patt):
        if half< index:
            if half+ num <= index:
                half += num
                list1.append(num)
                patt[i]=0
        else:
            break
    return [i for i in patt if i!=0], list1
            
# The best answer --->
def create_two_sets_of_equal_sum(n):
    if n % 4 in {1, 2}: return []
    return [[*range(1,n//4+1), *range(n*3//4+1,n+1)], [*range(n//4+1,n*3//4+1)]]
         
    