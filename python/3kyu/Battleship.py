"""Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.


Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell."""


# --------------------- answer ---------->

import re
def validate_battlefield(field):
    result = []
    result2=[]
    patt = {"1": 4, "11": 3, "111": 2, "1111": 1}
    lst = [0 for i in range(12)]
    for ls in field:
        ls.append(0)
        ls.insert(0, 0)

    field.append(lst)
    field.insert(0, lst)

    revers_field=[]
    for lst in field:
        if len(find:=[ship for ship in re.findall("([1]+)","".join([str(num) for num in lst])) if len(ship)>1])>0:
            result.append(find)
    for a in range(12):
        temp =[]
        for b in range(12):
            temp.append(str(field[b][a]))
        revers_field.append(temp)
    for lst in revers_field:
        if len(find:=[ship for ship in re.findall("([1]+)","".join([str(num) for num in lst])) if len(ship)>1])>0:
            result.append(find) 
    for a in range(1,11):
        for b in range(1,11):
            if field[a][b]==1 and field[a][b-1]== 0 and field[a][b+1]==0:
                if field[a-1][b-1]==1 or  field[a-1][b+1]==1 or  field[a+1][b-1]==1 or  field[a+1][b+1]==1:
                    return False 
                if revers_field[b][a-1]=="0" and revers_field[b][a+1]=="0":
                    result2.append("1")      
            
    final=[]
    for ls in result:
        for pat in ls:
            result2.append(pat)           
    for check in result2:
        if check not in patt:
            return False
        if result2.count(check)!= patt[check]:
            return False
    if len(result2)!=10:
        return False
    return True

            





# best solution-->:
from scipy.ndimage.measurements import label, find_objects, np
def validate_battlefield(field):
    field = np.array(field)
    return sorted(
        ship.size if min(ship.shape) == 1 else 0
        for ship in (field[pos] for pos in find_objects(label(field, np.ones((3,3)))[0]))
    ) == [1,1,1,1,2,2,2,3,3,4]