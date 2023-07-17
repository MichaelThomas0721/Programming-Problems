# Version 1. Beats about 50% on speed. Looking at the top answers it seems they do basically the same thing except
# Not using the Counter()

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        cnt = Counter(s1)
        pCnt = Counter(s2[0:len1])
        if cnt == pCnt: return True
        for r in range(len1, len2):
            pCnt[s2[r-len1]] -= 1
            pCnt[s2[r]] = pCnt.get(s2[r], 0)+1
            if cnt == pCnt:
                return True

        return False

    s1 = "ab"
    s2 = "eidbaooo"
    s1 = "ab"
    s2 = "eidboaoo"
    s1 = "adc"
    s2 = "dcda"
    s1 = "abc"
    s2 = "cccccbabbbaaaa"
    print(checkInclusion(1, s1, s2))