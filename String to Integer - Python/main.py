# Version 1, Not great honestly, only beats about 50% for speed and 10% for mem on leet code. I got tripped up on the wording and edge cases for a while.
# I can definitely do better, it just took me a while to understand extactly what they meant.

# Version 2, Much better, still only beats around 65% on speed but beats 97.5% on mem. Since this is a fairly easy question, running the test multiple times
# results in varying scores. 

# Version 3, I changed the .strip to .lstrip to increase the speed at the expense of some memory and WOW, right away I got 99.86% on speed. I'm calling this one
# a win for sure. I think I could make it faster by getting all the numbers first then converting but I found this way more fun :)

class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        started = False
        sign = None
        s = s.lstrip()
        while s:
            newChar = s[0]
            s = s[1:]
            try:
                newNum = int(newChar)
                started = True
                num *= 10
                num += newNum
            except:
                if (newChar == "-" or newChar == "+") and sign == None and not started:
                    if newChar == "-":
                        sign = True
                    else:
                        sign = False
                    started = True
                else:
                    s = ""
        if (sign): num *= -1
        if (num > 2147483647): return 2147483647
        elif (num < -2147483648): return -2147483648
        return num
    

    tests = [["42", 42], ["   -42asdf 34", -42], ["4193 with words", 4193], ["words and 987", 0], ["-91283472332", -2147483648], ["+1", 1], ["+-12", 0], ["21474836460", 2147483647], [".1", 0]]
    for test in tests:
        print(myAtoi(1, test[0]) == test[1])