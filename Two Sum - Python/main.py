# Version 1. Beats around 40% for speed and 94% for mem but I would like to speed it up, I think I am gonna try a hashset
# Version 2. Ya so a hashset is just way faster. Jumped right up to 97.4% and I think I could make it better if I spent more time on it
# The solution I write is also a little complicated and not easy to read so I would probably want to find a better solution if this was
# for production.

class Solution:
    def twoSum(self, nums, target: int):
        hashset = set(nums)
        for n in nums:
            oNum = target - n
            if oNum in hashset:
                rNums = [nums.index(n), nums.index(oNum)]
                if rNums[0] == rNums[1]:
                    tempNums = nums.copy()
                    del tempNums[rNums[0]]
                    hashsetT = set(tempNums)
                    if oNum in hashsetT:
                        return [rNums[0], tempNums.index(oNum) + 1]
                else:
                    return [nums.index(n), nums.index(oNum)]

        # removed = 0
        # for n in nums:
        #     oNum = target - n
        #     nums = nums[1:]
        #     removed += 1
        #     if oNum in nums:
        #         rNums = [removed - 1, removed + nums.index(oNum)]
        #         return rNums

    tests = [[[[2,7,11,15], 9], [0,1]], [[[3,2,4], 6], [1,2]], [[[3,3], 6], [0,1]]]

    for test in tests:
        print("RETURN: ", twoSum(1, test[0][0], test[0][1]))# == test[1])

    # print(twoSum(1, tests[0][0][0], tests[0][0][1]) == tests[0][1])