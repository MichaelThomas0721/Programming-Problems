# Version 1. Kinda good, between 50% and 80% but I just learned about a str.count() function and I'm going to try that out
# Version 2. Wow that is a lot faster. 99.5% speed

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        chars = set(s)
        for idx in chars:
            if s.count(idx) != t.count(idx): return False
        return True
    
    tests = [[["anagram", "nagaram"], True], [["rat", "car"], False]]

    for test in tests:
        print(isAnagram(1, test[0][0], test[0][1]) == test[1])
    
    # print(isAnagram(1, tests[0][0][0], tests[0][0][1]) == tests[0][1])