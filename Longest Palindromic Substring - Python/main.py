# Version 1 completed, accepted by LeetCode. Incredibly slow and unoptimized but works. Will improve later.

def nextChars(s, middle, index, ls, rs):
    return [s[middle-index-ls], s[middle+index+rs]]
def nextChar(s, middle, index, dir):
    return s[middle+(index*dir)]
def longestSame(s, middle, dir, startingLetter, dirMid):
    dirSame = 1
    for i in range(1, dirMid + 1):
        currentC = nextChar(s, middle, i, dir)
        if (currentC != startingLetter):
            break
        dirSame = i
    return dirSame
def getString(s, middle, ls, rs, length):
    return s[middle-ls-length:middle+rs+length+1]
def findDirLength(middle, length, dir, offset):
    return abs(length - middle - (offset * dir))
def findPalindrome(s, middle):
    nextC = nextChars(s, middle, 1, 0, 0)
    startingLetter = s[middle]
    ls = 0
    rs = 0
    leftDirMid = (findDirLength(middle, 0, -1, 0))
    rightDirMid = (findDirLength(middle, len(s), 1, 0)) - 1
    if (nextC[0] == startingLetter):
        ls = longestSame(s, middle, -1, startingLetter, leftDirMid)
    if (nextC[1] == startingLetter):
        rs = longestSame(s, middle, 1, startingLetter, rightDirMid)
    if (rs + ls == len(s)-1):
        return s
    elif (rs + ls == len(s)-2):
        return s[middle-ls:middle+rs+1]
    elif (middle - ls == 0 or middle + rs == len(s)-1):
        return s[middle-ls:middle+rs+1]
    leftDirMid = (findDirLength(middle, 0, -1, ls))
    rightDirMid = (findDirLength(middle, len(s), 1, rs)) - 1
    shortestDirMid = min(leftDirMid, rightDirMid) + 1
    length = 0
    for i in range(1, shortestDirMid):
        nextC = nextChars(s, middle, i, ls, rs)
        if (nextC[0] != nextC[1]):
            length = i-1
            break
        length = i
    return (getString(s, middle, ls, rs, length))

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if (length == 0):
            return ""
        if (length == 1):
            return s
        if (length == 2):
            if (s[0] == s[1]):
                return s
            return s[0]
        middle = int(length/2)
        longest = ""
        leftDirMid = (findDirLength(middle, 0, -1, 0))
        rightDirMid = (findDirLength(middle, len(s), 1, 0)) - 1
        longestDirMid = max(leftDirMid, rightDirMid)
        for i in range(longestDirMid):
            if (leftDirMid > i):
                leftPal = (findPalindrome(s, middle-i))
            if (rightDirMid > i):
                rightPal = (findPalindrome(s, middle+i))
            longestPal = max(leftPal, rightPal, key=len)
            if (len(longestPal) > len(longest)):
                longest = longestPal
        return longest


    s = "faafasdfasdfahgfdsfhsdfgaaaf"
    print(longestPalindrome(1, s))