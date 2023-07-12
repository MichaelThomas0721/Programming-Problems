# Version 1. Accepted by leetcode but quite slow. Looking at other solution I realized my first thought was actually
# The correct one but I thought it would've been slower. I decided to use a hash set and it is a lot slower apparently.

# Version 2. Is faster and more reliable, similar to version 1 though

class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) <= 1: return len(nums)
        hashset = set(nums)
        ans = 0
        for num in hashset:
            if num-1 in hashset:
                continue
            c = 1
            cn = num
            while cn+1 in hashset:
                c += 1
                cn += 1
            if c > ans:
                ans = c
        return ans
        # while len(hashset) > 0:
        #     num = next(iter(hashset))
        #     current = [num]
        #     start = num
        #     prev = start
        #     hashset.remove(num)
        #     while True:
        #         if prev+1 in hashset:
        #             prev = prev+1
        #             current.append(prev)
        #             hashset.remove(prev)
        #         else:
        #             break
        #     prev = start
        #     while True:
        #         if prev-1 in hashset:
        #             prev = prev-1
        #             current.append(prev)
        #             hashset.remove(prev)
        #         else:
        #             break
        #     if len(current) > ans:
        #         ans = len(current)
        # return ans

    print(longestConsecutive(1, [100, 4, 200, 1, 3, 2]))
    print(longestConsecutive(1, [0,3,7,2,5,8,4,6,0,1]))
    print(longestConsecutive(1, [0, -1]))