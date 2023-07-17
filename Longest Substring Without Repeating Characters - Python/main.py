# Version 1. Faster than 80% on speed but less than 50% on mem. Not sure how to make it more memory efficient at the time


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = set()
        ans = 0
        for char in s:
            if char in count:
                while char in count:
                    count.remove(s[l])
                    l += 1
            count.add(char)
            ans = max(ans, len(count))
        return ans
    s = "dabcabcbb"
    print(lengthOfLongestSubstring(1, s))