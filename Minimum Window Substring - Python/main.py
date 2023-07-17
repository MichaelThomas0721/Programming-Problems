# Version 1. Not super fast, only beats around 43% on speed and 65% on mem. Currently I'm doing more of an inchworm rather than a slider window.
# The right goes up, than the left goes up, etc.
# I could change it so that the left pointer moves with the right one once a match has been found but I'm not sure if that would be more efficient
# so I will leave it for now.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        for char in t:
            tCount[char] = 1 + tCount.get(char, 0)
        l = 0
        sCount = {}
        ans = ""
        have, need = 0, len(tCount)
        for r, char in enumerate(s):
            if char in t:
                sCount[char] = 1 + sCount.get(char, 0)
                if sCount[char] == tCount[char]:
                    have += 1
                while have == need:
                    if len(ans) > r-l or ans == "":
                        ans = s[l:r+1]
                    if s[l] in t:
                        sCount[s[l]] -= 1
                        if sCount[s[l]] < tCount[s[l]]:
                            have -= 1
                    l += 1
        return ans

    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(1, s, t))