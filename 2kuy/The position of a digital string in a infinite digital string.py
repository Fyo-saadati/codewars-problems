import re
def find_position(string):
    numbers=list(map(lambda num: int(num), string))
    patt= {100: 189, 1000: 2889, 10000: 38889, 100000: 488889, 
           1000000: 5888889, 10000000: 68888889, 100000000: 788888889, 
           1000000000: 8888888889, 10000000000: 98888888889, 
           100000000000: 1088888888889, 1000000000000: 11888888888889, 
           10000000000000: 128888888888889}
    if (( numbers[-1]*(numbers[-1]+1))//2)-(( (numbers[0]-1)*((numbers[0]-1)+1))//2)== sum(numbers):
        return numbers[0]-1

def num(string):
    num=1
    patt=""
    while str(string) not in patt:
        patt += str(num)
        num +=1
    pos=re.search(f"{str(string)}", patt)
    return pos.span()[0]

def get_dic():
    dic={}
    num=100
    summand1=9
    summand2=2
    for i in range(12):
        times= int(f"9{i*'0'}1")
        dic[num]=(summand1+(times*summand2)) - summand2
        summand1= (summand1+(times*summand2)) - summand2
        summand2 +=1
        num *=10



