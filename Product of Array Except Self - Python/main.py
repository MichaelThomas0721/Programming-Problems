# Version 1. Honestly thought it would be faster, after looking at tutorials I am not sure why it isn't, scores 40% for speed and 50% for mem if I am lucky
# Would love to revisit and figure out why it is so slow. I'm guessing I am using leetcode at a bad time but I could be wrong.

class Solution:
    def productExceptSelf(self, nums):
        l = len(nums)
        ans = [1] * l
        pre = 1
        post = 1

        for i in range(l):
            ans[i] *= pre
            ans[l-i-1] *= post
            pre *= nums[i]
            post *= nums[l-i-1]
        return ans
    
    nums = [1,2,3,4,5]
    print(productExceptSelf(1,nums))

    # Faster but uses division
        # total = 1
        # zeros = 0
        # for num in nums:
        #     if num != 0:
        #         total *= num
        #     else:
        #         zeros += 1
        #         if (zeros >= 2):
        #             total = 0
        #             break
        # ans = []
        # for num in nums:
        #     if (num == 0): ans.append(int(total))
        #     elif zeros == 0:
        #         ans.append(int(total/num))
        #     else:
        #         ans.append(0)
        # return ans