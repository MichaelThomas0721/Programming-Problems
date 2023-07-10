# Version 1, I clearly misunderstood the question and the test cases seem a little misleading/uninformative to me so I will come back to this later.
# I don't want to follow a tutorial since I want to figure it out myself but the wording doesn't really make sense to me right now.

class Solution:
    def removeLast(self, s: str, p: str) -> object:
        return [ s[1:], p[1:]]

    def isMatch(self, s: str, p: str) -> bool:
        prev = ""
        while s and p:
            if s[0] == p[0]:
                prev = s[0]
                s, p = self.removeLast(s, p)
            elif p[0] == ".":
                prev = s[0]
                s, p = self.removeLast(s, p)
            elif p[0] == "*":
                prev = s[0]
                s, p = self.removeLast(s, p)
                while s and p:
                    if s[0] != prev:
                        return False
                    else:
                        s = s[1:]
                    p = p[1:]
            else: return False
        if not s: return True
        else: return False
    

    def __init__(self):
        tests = [[["aa", "a"], False], [["aa", "a*"], True], [["ab", ".*"], True], [["aab", "c*a*b"], True]]

        for test in tests:
            print(self.isMatch(test[0][0], test[0][1]) == test[1])

        # print(self.isMatch(tests[0][0][0], tests[0][0][1]))
    
solution = Solution()