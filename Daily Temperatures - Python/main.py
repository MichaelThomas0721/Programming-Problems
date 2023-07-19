# Version 1. Not super fast or memory efficient. Lands in the range of 35%-75% so not great but alright.
# Nevermind, the faster answer do pretty much the same thing just luckier I guess?

class Solution:
    def dailyTemperatures(self, temperatures):
        # Create a stack that will store the temperature and index
        ans = [0] * len(temperatures)
        stack = []
        # Loop through each number in the temperatures array
        for i, t in enumerate(temperatures):
        # If the current temperature is greater than the top element in the stack, set the ans for that top element to the current temp (indexes - eachother)
        # Loop that until it is empty or the top element is greater
            while stack and t > stack[-1][0]:
                st, si = stack.pop()
                ans[si] = i - si
        # Add the current temp to the stack
            stack.append([t,i])
        return ans




    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(1, temperatures))