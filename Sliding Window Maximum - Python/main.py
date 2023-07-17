# Not my answer, just trying to understand it :)

import collections

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        output = []
        q = collections.deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output


    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    # nums = [1]
    # k = 1
    print(maxSlidingWindow(1, nums, k))