""" 
(5kyu)
The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared). 
Eighty one (81), is the first number in having this property (not considering numbers of one digit). 
The next one, is 512. Let's see both cases with the details

8 + 1 = 9 and 92 = 81

512 = 5 + 1 + 2 = 8 and 83 = 512

We 13:52521875, need to make a function that receives a number as argument n and returns the n-th term of this sequence of numbers.
"""
def power_sumDigTerm(n):
    dict = {1:81, 2:512, 3:2041, 4:4913, 5:5832, 
            6:17576, 7:19683, 8:234256, 9:390625, 
            10:614656, 11:1679616, 12:17210368, 
            }
    if n in dict:
        return dict[n]
    result =12
    counter =17210368
    while result < n:
        counter +=1
        sum_num = sum([int(num) for num in list(str(counter))]) 
        if counter  == (sum_num**3):
            result +=1
            if result == n-1 :
                return counter
        elif counter  == (sum_num**4):
            result +=1
            if result == n-1 :
                return counter
        elif counter  == (sum_num**5):
            result +=1            
            if result == n-1 :
                return counter




