# Version 1. Consistantly beats 92%+ on speed. The solution is a bit complicated and looking at the ones that beat
# mine, its a similar concept just using operators I have never used before. I could have also done a 2 pointer
# solution but I'm pretty sure that would have been a lot slower. Just a guess though.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1: return True
        # Remove Spaces
        s = ''.join(filter(str.isalnum, s))
        # Split in half
        l = len(s)
        hL = int(l/2)
        s1 = s[0:hL]
        s2 = s[hL:l]
        if l % 2 != 0: s2 = s2[1:]
        # Reverse the second half
        s2 = list(s2)
        s2.reverse()
        s2 = ("").join(s2)
        s1 = s1.lower()
        s2 = s2.lower()
        # Check if the halfs equal eachother
        if s1 == s2: return True
        return False



    pal = "A man, a plan, a canal: Panama"
    # pal = "1234"
    print(isPalindrome(1, pal))