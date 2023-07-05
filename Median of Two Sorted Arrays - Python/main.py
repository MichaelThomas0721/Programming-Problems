# Working solution, beat 93.90% on leetcode (Speed)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        length = len(nums3)
        solution = 0
        if length % 2 != 0:
            solution = (nums3[int(length/2 - 0.5)])
        else:
            solution = ((nums3[int(length/2 - 1)] + nums3[int(length/2)]) / 2)
        return solution

    arr1 = [1,2]
    arr2 = [3]

    print(findMedianSortedArrays(1, arr1, arr2))