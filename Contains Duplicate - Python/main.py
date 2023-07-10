# Version 1. Ok solution, beats around 50% for speed and mem but can go up to 85%, not really sure how to improve atm though
# Version 2. I've been writing code like javascript lol, changed the for loop to be a bit more efficient, no longer "i in range(len(nums))"
# Ok, looking at the top answers it looks like they just open the Output file and print it, so I think this is as fast as it is going to get (realistically)

class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    tests = [[[1,2,3,1], True], [[1,2,3,4], False], [[1,1,1,3,3,4,3,2,4,2], True]]

    for test in tests:
        print(containsDuplicate(1, test[0]) == test[1])