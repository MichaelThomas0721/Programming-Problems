# Version 1, incredibly slow, it did work but wasn't fast enough
# Version 2, I had the right idea just kinda had to go outside in which makes sense

class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]
        ans = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r]
        return ans

    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [0,0,0,0,3,0,0,0]
    # height = [4,2,0,3,2,5]
    # height = [1000,999,998,997,996,995,994,993,992,991,990,989,988,987,986,985,984,983,982,981,980,979,978,977,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966]
    print(trap(1, height))