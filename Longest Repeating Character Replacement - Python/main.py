# Version 1. Kinda slow, forgot that I don't really need to make the window smaller since I am just looking for the longest length
# So I can just continue forward without worrying about it. Will fix it in version 2
# Version 2. Much faster

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxL = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxL = max(count[s[r]], maxL)
            if (r - l + 1) - maxL > k:
                count[s[l]] -= 1
                l += 1
        return r-l+1
        
    # s = "ABAB"
    # k = 2
    # s = "AABABBA"
    # k = 1
    s = "ABAA"
    k = 0
    print(characterReplacement(1, s, k))