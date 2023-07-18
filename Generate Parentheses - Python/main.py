# Version 1. Beats about 62.5% on speed which isn't bad but not great.

class Solution:
    def generateParenthesis(self, n: int):
        if n == 0: return []
        ans = ["("]
        while True:
            completed = True
            newAns = []
            for a in ans:
                if a.count("(") == n:
                    while a.count(")") < n:
                        a += ")"
                        newAns.append(a)
                else:
                    b = (a + '.')[:-1]
                    a += "("
                    if b.count("(") > b.count(")"):
                        b += ")"
                        newAns.append(b)
                    newAns.append(a)
                    completed = False
            ans = newAns
            if completed: return ans



        print("E")

    
    print(generateParenthesis(1, 7))