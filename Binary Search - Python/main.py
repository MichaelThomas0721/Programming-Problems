# Version 1. This is just some regular binary search so pretty straight forward.
# Faster than 83%

class Solution:
    def search(self, nums, target: int) -> int:
        # Get the middle integer, if it is higher, get the middle of the first integer, etc...abs
        prevL = -1
        prevH = len(nums)
        current = int(len(nums)/2)
        num = nums[current]
        while not num == target and not prevH <= prevL + 1:
            if num > target:
                prevH = current
                current = int((current - prevL) / 2) + prevL
            else:
                prevL = current
                current = int((prevH - current) / 2) + current
            num = nums[current]
        if num == target: return current
        return -1
    
    nums = [-1,0,3,5,9,12]
    target = 9
    # nums = [-1,0,3,5,9,12]
    # target = 2

    print(search(1, nums, target))