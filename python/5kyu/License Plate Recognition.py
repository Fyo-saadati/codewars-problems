"""You have been hired by a company making speed cameras. 
Your mission is to write the controller software turning the 
picture taken by the camera into a license plate number.

Specification
The sensor matrix outputs a 3-line string using pipes and underscores. 
We want to translate this into a string with regular digits when these are recognized, 
and a ? when they are not. See the input and output examples below.

we plan to sell to various countries, so we make no assumption on length
there are no 0s or 1s on license plates
the input string sometimes misses one of the bottom two horizontal stripes. 
Since there is no ambiguity, we must return the digit instead of a question mark
Input
A non-empty string with pipes and underscores. It will always have 3 lines of identical 
length (which will always be a multiple of 3).

 _  _        _  _  _  _ \n
 _| _||_||_ |_   || ||_|\n
|_  _|  | _|| |  ||_| _|"""

#---answer -- - ->:
import re
def recognize(s):
    
    regex = r' _ \n _\|\n\|_ '
    text = ' _ \n _|\n|_ '
    print(text)



    match = re.match(regex, s[1])
    print(match)





    
    
    
s =     (
        'Plate with some missing, one error',
        ' _  _     _     _  _  _ \n'
        ' _|  ||_||_ |_   ||_|| |\n'
        '|_  _|  |  ||_|  || | _|',

        '2345?789'
    )
recognize(s)


