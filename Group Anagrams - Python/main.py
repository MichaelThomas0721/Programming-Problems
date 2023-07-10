# Version 1, Ok solution beats 80% for speed but only 37% for mem. Maybe I'll revisit to improve later. A really fun challenge though. 

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        dict = defaultdict(list)
        if len(strs) <= 1:
            return [strs]

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - 97] += 1
            dict[tuple(arr)].append(s)
            
        ans = []
        for l in dict:
            ans.append(dict[l])
        return ans
    tests = [[["eat","tea","tan","ate","nat","bat"],[["bat"],["nat","tan"],["ate","eat","tea"]]], [[""], [[""]]], [["a"], [["a"]]]]

    for test in tests:
        print(groupAnagrams(1, test[0]) == test[1])

    # print(groupAnagrams(1, tests[0][0]) == tests[0][1])