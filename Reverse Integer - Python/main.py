# Version 1, pretty good, beats 85% for speed and 95% for memory on leetcode

class Solution:
    def reverse(self, x: int) -> int:
        sign = False
        if (x < 0): sign = True
        x = abs(x)
        reversed = 0
        while x:
            newNum = x % 10
            x = int(x/10)
            reversed *= 10
            reversed += newNum
        if (reversed > 2147483647): return 0
        if (sign): reversed *= -1
        return reversed


    tests = [1234, 523732, 239482, 234291, 32434, -123, 1534236469]

    for test in tests:
        print(reverse(1, test))
