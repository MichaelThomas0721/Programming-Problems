# This one was really hard honestly, I spent a really long time trying to figure it out and just couldn't. I think stack
# Is something I will need to return to and work on.

class Solution:
    def largestRectangleArea(self, heights) -> int:
        maxArea = heights[0]
        stack = []

        for i, height in enumerate(heights):
            while stack and stack[-1][1] > height:
                index, nHeight = stack.pop()
                maxArea = max(maxArea, nHeight * (i - index))
            stack.append([i, height])
        for i, h in stack:
            maxArea = max(maxArea, h *(len(heights) - i))
        return maxArea
    
    heights = [2,1,5,6,2,3]
    print(largestRectangleArea(1, heights))