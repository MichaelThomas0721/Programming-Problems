# Version 1, honestly probably not the most elegant solution but it works and beats 93% so that's alright I guess.

class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()
        # Loop through each number
        for index, num in enumerate(nums):
            if num > 0:
                break

            if index > 0 and num == nums[index - 1]:
                continue
        # Create pointers on outsides
            r = len(nums) - 1
            l = index+1
            while r > l:
                total = num + nums[r] + nums[l]
                if total == 0:
                    ans.append([num, nums[r], nums[l]])
                    l+= 1
                    while nums[l] == nums[l-1] and r > l:
                        l+= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return ans
        # Check if the numbers added is more or less
        # Adjust the appropriate pointe

    nums = [-1,0,1,2,-1,-4]
    print(threeSum(1, nums))