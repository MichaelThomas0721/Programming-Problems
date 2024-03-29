# Version 3 completed, accepted by LeetCode. Made it so it doesn't loop over duplicate letters, thought it might save some time but didn't do much.
def findSame(s, length, sc, idx, dir):
    while (idx >= 0 and idx < length and s[idx] == sc):
        idx += dir
    return idx
def findPalindrome(s, middle, length):
    if middle == 0:
        return [s[0], []]
    elif middle == length - 1:
        return [s[length - 1], []]
    sc = s[middle]
    leftIdx = middle - 1
    rightIdx = middle + 1
    if leftIdx >= 0:
        leftIdx = findSame(s, length, sc, leftIdx, -1)

    else:
        leftIdx += 1
    if rightIdx < length:
        rightIdx = findSame(s, length, sc, rightIdx, 1)
    else:
        rightIdx -= 1
    sames = []
    if (leftIdx - rightIdx > 3):
        sames = [leftIdx, rightIdx]
    while (leftIdx >= 0 and rightIdx < length):
        if (s[leftIdx] != s[rightIdx]):
            break
        leftIdx -= 1
        rightIdx += 1
    return [s[leftIdx + 1:rightIdx], sames]
         


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if (length == 0):
            return ""
        elif (length == 1):
            return s
        elif (length == 2):
            if (s[0] == s[1]):
                return s
            return s[0]
        middle = int(length/2)
        leftIdx = middle - 1
        rightIdx = middle
        left = False
        longest = ""
        longestLen = 0
        while leftIdx >= 0 and rightIdx < length:
            if left:
                pal = findPalindrome(s, leftIdx, length)
                if pal[1] != []:
                    leftIdx = pal[1][0]
                    rightIdx = pal[1][1]
                pal = pal[0]
                if (len(pal) > longestLen):
                    longest = pal
                    longestLen = len(pal)
                leftIdx -= 1
                left = False
            else:
                pal = findPalindrome(s, rightIdx, length)
                if pal[1] != []:
                    leftIdx = pal[1][0]
                    rightIdx = pal[1][1]
                pal = pal[0]
                if (len(pal) > longestLen):
                    longest = pal
                    longestLen = len(pal)
                rightIdx += 1
                left = True
        return longest



    s = "adfaaaaafm"
    print(longestPalindrome(1, s))