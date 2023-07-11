# Version 1. I am using a collection to get the counts for all the numbers then finding the greatest one. Very slow but great on memory, will try again.
# Instead of finding

import collections

class Solution:
    def topKFrequent(self, nums, k: int):
        count = collections.Counter(nums)
        print(count)
        count = sorted(count.items(), key=lambda x:x[1], reverse=True)[:k]

        return list(list(zip(*count))[0])

        # Old garabage
        # for num in count:
        #   ans.append(num[0])
        # return ans
        # return (count[0:k])

        # ans = []
        # for i in range(k):
        #     gNum = max(count, key=count.get)
        #     ans.append(gNum)
        #     del count[gNum]

        # return ans

    test = [[1, 1, 1, 2, 2, 3], 2]

    print(topKFrequent(1, test[0], test[1]))