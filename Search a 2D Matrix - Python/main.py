# Version 1. Not sure if very slow or not since it lands between 7% and 80% depending on the run. I also saw the memory get up to 93% but as low as 15%.
# Looking at the top answers, they are generally the same method of solving so I'm going to leave it.

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        la = 0
        ra = len(matrix) - 1
        arr = -1
        while la <= ra:
            m = la + ((ra - la) // 2)
            if matrix[m][0] > target:
                ra = m - 1
            elif matrix[m][-1] < target:
                la = m + 1
            else: 
                arr = m
                break
        if arr == -1: return False
        l = 0
        r = len(matrix[arr]) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[arr][m] > target:
                r = m - 1
            elif matrix[arr][m] < target:
                l = m + 1
            else: return True
        return False


    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    matrix = [[1]]
    target = 2
    matrix = [[1,3]]
    target = 3


    print(searchMatrix(1, matrix, target))