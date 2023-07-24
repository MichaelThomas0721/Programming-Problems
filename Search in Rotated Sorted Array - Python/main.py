# Version 1. I had to look up an explanation for this one and I am still a little confused so I will come back to it later.

class Solution:
    def search(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + ((r-l)//2)
            if nums[m] == target: return m
            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        if nums[l] == target: return l
        if nums[r] == target:  return r
        return -1
    
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(1, nums, target))