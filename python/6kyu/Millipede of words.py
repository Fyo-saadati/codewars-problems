"""
(6kyu)
The set of words is given. Words are joined if the last letter of one word and the first letter of another word are the same. Return true if all words of the set can be combined into one word. Each word can and must be used only once. Otherwise return false.

Input
List of 3 to 7 words of random length. No capital letters.

Example true
Set: excavate, endure, desire, screen, theater, excess, night.
Millipede: desirE EndurE ExcavatE ExcesS ScreeN NighT Theater.

Example false
Set: trade, pole, view, grave, ladder, mushroom, president.
Millipede: presidenT Trade.

"""


def solution(arr):
    first_ch = [word[0] for word in arr]
    last_ch = [word[-1] for word in arr]
    first = ""
    last = ""
    for i, ch in enumerate(first_ch):
        if first_ch.count(ch) == 1:
            first += arr.pop(i)
        elif last_ch.count(ch) == 1:
            last += arr.pop(i)
    print(last)
    if len(first) != 0:
        string1 = first
        for i in range(len(arr)):
            for word1 in arr:
                if word1 not in string1 and word1[0] == string1[-1]:
                    string1 += word1
        if len(string1) == len("".join(arr)):
            return True

    elif len(last) != 0:
        for i in range(len(arr)):
            string2 = last
            for word1 in arr:
                if word1 not in string2 and word1[-1] == string2[0]:
                    string2 = word1 + string2
        if len(string2) == len("".join(arr)):
            return True
    else:
        string3 = arr[0]

        for i in range(len(arr)):
            for word2 in arr:
                if word2 not in string3 and word2[0] == string3[-1]:
                    string += word2
                if word2 not in arr and word2[-1] == string3[0]:
                    string3 = word2 + string3
        if len(string3) == len("".join(arr)):
            return True
    return False


print(solution(["excavate", "thesis", "effort", "endure", "triangle", "endorse"]))
