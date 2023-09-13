"""You are given a list/array of example equalities such as:

[ "a + a = b", "b - d = c ", "a + b = d" ]
Use this information to solve a given formula in terms of the remaining symbol such as:

formula = "c + a + b"
In this example:

"c + a + b" = "2a"
so the output is "2a".

Notes:

Variables names are case sensitive.
There might be whitespaces between the different characters. Or not...
There should be support for parentheses and their coefficient. Example: a + 3 (6b - c).
You may encounter several imbricated levels of parentheses, but you'll get only constant terms 
for the accompanying coefficients (never variables).
All equations will be linear.
In your final answer, include a leading 1 when the coefficient is 1 (e.g. 1j instead of just j).
There are no floating-point numbers.
See the sample tests for clarification on what exactly the input/ouput formatting should be.

Without giving away too many hints, the idea is to substitute the examples into the formula and 
reduce the resulting equation to one unique term. Look carefully at the example tests: you'll 
have to identify the pattern used to replace variables in the formula/other equations. Using this 
pattern, only one solution is possible for each test, so if you keep asking yourself "but what if 
instead of that I do...", then you've missed the pattern.
"""
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
    while patternChecker(pattern) == True:
        for key1 in pattern:
            for key2 in pattern:
                if "(" in pattern[key2]:
                    replaced = parenthesesRemover(pattern[key2])
                    pattern[key2]=pattern[key2].replace(replaced[1], replaced[0] )
                elif key1 in pattern[key2]:
                    pattern[key2]=(replaced:=replacment(pattern[key2], pattern))
                    replaced = parenthesesRemover(replaced)
                    pattern[key2]=pattern[key2].replace(replaced[1], replaced[0] )
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



print(simplify(['y + 6Y - k -         6 K = f', 'F + k + Y - y = K', 'Y = k',"y = Y", "y + Y = F"],"k - f+5(10(-25(12(K+2(25Y+y))))) + y",))


