# Version 1. Works and is fast but kinda sucks on memory, not sure how I would do it fast and memory efficient at the moment so maybe I will come back another day.

import collections

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        stack = collections.deque()
        l = 0
        ans = []
        for i, num in enumerate(nums):
        # Remove the numbers on the right of the stack that are less than the current number
            while stack and nums[stack[-1]] <= num:
                stack.pop()
            stack.append(i)
        # If the left most number is less than the left pointer, remove it
            if stack[0] < l:
                stack.popleft()
        # The max is the left most number
            if i+1 >= k:
                ans.append(nums[stack[0]])
                l += 1

        return ans

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    # nums = [1]
    # k = 1
    # nums = [1,-1]
    # k = 1
    print(maxSlidingWindow(1, nums, k))