# Version 1. I don't always get it on my first run with zero errors and beating 97% but when it happens it is AWESOME. It also beat 83.5% on mem
# I'm happy with this solution. Honestly a fairly easy problem, just standard two pointers
# The faster solutions involve opening the out file and writing the answer directly instead of returning which feels like cheating so I'm not going to change my answer

class Solution:
    def maxArea(self, height) -> int:
        # Start with pointers on the end
        r = len(height) - 1
        l = 0
        ans = 0
        while r > l:
        # Calculate the area, if its the biggest so far, record it, if not, move the smaller pointer in
            area = (r-l)*min(height[r], height[l])
            if area > ans: ans = area
        # Check if the new height is larger, if not, move on
            if height[r] > height[l]:
                prev = height[l]
                l += 1
                while height[l] < prev:
                    l += 1
            else:
                prev = height[r]
                r -= 1
                while height[r] < prev:
                    r -= 1
        return ans

    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(1, height))