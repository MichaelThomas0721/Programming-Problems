# Version 1. Beats 90% for speed. I could check if the answer is half the target twice before and probably speed up
# the process a little bit but I'll move on for now, maybe come back and try it out.

class Solution:
    def twoSum(self, numbers, target: int):
        # Put numbers in a set
        hashset = set(numbers)
        # Start with first number in array and see if the (target-num) is in the set
        # If target/2 is in set, check if it appears twice, if not, move on
        for index, num in enumerate(numbers):
            v = int(target - num)
            if v in hashset:
                idx2 = numbers.index(v)
                if index != idx2:
                    return [index+1, idx2+1]
                elif numbers.count(num) > 1:
                    del numbers[idx2]
                    idx2 = numbers.index(num)+1
                    return [index+1, idx2+1]
    
    nums = [2,3,4]
    target = 6
    # nums = [0,0,3,4]
    # target = 0
    print(twoSum(1, nums, target))