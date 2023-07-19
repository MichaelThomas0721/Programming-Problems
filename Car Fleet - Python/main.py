# Version 1. This seemed really difficult at first ngl, I came up with a solution pretty quick but genuinly thought it was too simple to work well
# but I ended up getting faster than 86% on the first run so that's something for sure.

class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        if len(position) <= 1: return len(position)
        # Sort the array
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        ans = 1
        time = (target - pair[0][0]) / pair[0][1]
        # Calculate the time for each one to arrive ie. (Target - position) / speed
        # Everytime a slower one is found, that is the new number to look for and add 1 to the ans
        for i in range(1, len(pair)):
            nTime = (target - pair[i][0]) / pair[i][1]
            if nTime <= time:
                continue
            else:
                time = nTime
                ans += 1
        return ans

    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(carFleet(1, target, position, speed))