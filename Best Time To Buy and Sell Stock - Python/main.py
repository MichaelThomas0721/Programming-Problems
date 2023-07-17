# Version 1. Beats 50-60% for speed. Can be better.
# Version 2. It was overcomplicated and now it is not.

class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        minP = prices[0]
        for num in prices:
            if num < minP: minP = num
            if num-minP > ans: ans = num-minP
        return ans

        # # Start with a pointer at the start and a pointer one in front
        # # Move to the right and if the price is higher than the previous highest right pointer than record the difference.
        # # If the right pointer is less than the left pointer, record the current difference and move the left pointer to the right
        # # Repeat
        # l = 0
        # r = 1
        # ans = 0
        # le = len(prices)
        # while r < le:
        #     if prices[r] < prices[l]:
        #         l = r
        #     elif prices[r] > prices[r-1]:
        #         ans = max(prices[r] - prices[l], ans)
        #     r += 1
        # return ans 

    
    # prices = [7,1,5,3,6,4]
    prices = [7,6,4,3,1]
    print(maxProfit(1, prices))