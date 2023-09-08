import re
from time import sleep

def parenthesesRemover(formula):
    parenthese=parenthesesFinder(formula)[-1]
    if (number1 := parenthese[:parenthese.index("(")]) in {"+":'1', "-":'-1', "":'1', "1":"+1"}:
        number1 ={"+":'1', "-":'-1', "":'1', "1": "+1"}[number1]
    allVariable= [x for x in re.findall("([-+]*[0-9]*[a-zA-Z]*)", parenthese[parenthese.index("("):]) if x !=""]
    
    for i, var in enumerate(allVariable):
        number2 = ''.join(re.findall("([+-]*[0-9]*)", var))
        par= var.replace(number2, "")
        if number2 in {"+":"+1", "-":"-1", "":"+1", "1":"+1"}:
            number2 = {"+":"+1", "-":"-1", "":"+1", "1":"+1"}[number2]
        allVariable[i]= f"{int(number1)*int(number2)}{par}" 
    return [''.join([x if x[0]=="-" else f"+{x}" for x in allVariable]).replace("++", "+"),  parenthese]

def replacment(formula, pattern):
    allVariable= [x for x in re.findall("([-+]*[0-9]*[a-zA-Z]*)", formula) if x !=""]
    print(allVariable)
    for key in pattern:
        for i, var in enumerate(allVariable):
            if key in var:
                allVariable[i]=allVariable[i].replace(key, f"({pattern[key]})")
    return ''.join(allVariable) 

def computing(finalString):
    for i,par in enumerate(allVar :=[x for x in re.findall("([+-]*[0-9]*[a-zA-Z]*)", finalString) if x !=""]):
        if (number:=re.findall("([+-]*[0-9]*)", par)[0])=="+" or number == "-":
           allVar[i]={"+":'1',"-":'-1'}[number]+par[1:] 
    result=""
    sortedVar=[[x for x in allVar if y in x] for y in set(re.findall("([a-zA-Z])",finalString))]
    for lst in sortedVar:
        addition= sum(list(map(lambda number: int(number),[x for x in re.findall("([+-]*[0-9]*)", "".join(lst)) if x != ""])))
        if addition>0:
            result += f"+{addition}{''.join(x for x in lst[0] if x not in'+-0123456789')}"       
        else:
            result += f"{addition}{''.join(x for x in lst[0] if x not in'+-0123456789')}"       
    if result[0]=="+":
        return result[1:]
    return result

def parenthesesFinder(formula):
    n = list(re.finditer(r'([-+]*[0-9]*[a-zA-Z]*[(])', formula))
    return [(newString:=formula[hint.start():])[:newString.index(")")+1] for hint in n]

def conditionCheker(formula, pattern):
    for key in pattern:
        if key in formula or "(" in formula:
            return True
    return False

def patternChecker(pattern):
    for key in pattern:
            for key2 in pattern:
                if "(" in pattern[key2] or key in pattern[key2]:
                    return True
    return False

def examplesSimplify(examples):
    pattern ={example[-1]:example[:-2] for example in [''.join(string.split()) for string in examples]}
    pattern = doubleRemover(pattern)
    a= 0
    while patternChecker(pattern) == True:
        for key1 in pattern:
            for key2 in pattern:
                if "(" in pattern[key2]:
                    replaced = parenthesesRemover(pattern[key2])
                    pattern[key2]=pattern[key2].replace(replaced[1], replaced[0] )
                    a +=1
                    print(f"{a}): {replaced[0]}--{pattern}")
                    print(".............................")
                elif key1 in pattern[key2]:
                    pattern[key2]=(replaced:=replacment(pattern[key2], pattern))
                    replaced = parenthesesRemover(replaced)
                    pattern[key2]=pattern[key2].replace(replaced[1], replaced[0] )
                    a +=1
                    print(f"{a}): {replaced[0]}--{pattern}")
                    print(".............................")
                
    return pattern

def doubleRemover(pattern):
    for key1 in pattern:
        for key2 in pattern:
            if key1 == (x:=re.findall("([a-zA-Z]+)",pattern[key2] )[0]):
                pattern[key2]= pattern[key2].replace(x, pattern[key1])
    return pattern
                                       
def simplify(examples,formula):
    examples= ["".join(x.split()) for x in examples]
    formula = ''.join(formula.split())
    pattern = examplesSimplify(examples)
    while conditionCheker(formula, pattern)== True:
        if "(" in formula:
            removed=parenthesesRemover(formula)
            formula= formula.replace(removed[1], removed[0])
        else:
            formula=replacment(formula, pattern)
            removed=parenthesesRemover(formula)
            formula= formula.replace(removed[1], removed[0])
    return computing(formula)    



print(simplify(['y + 6Y - k - 6 K = f', 'F + k + Y - y = K', 'Y = k',"y = Y", "y + Y = F"],"k - f + y",))


