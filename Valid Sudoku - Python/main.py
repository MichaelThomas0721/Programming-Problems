# Version 1. A little complicated, probably a little more complicated than it needed to be but I was able to beat
# 95.4% on one of my submits so it seems alright. This question is fairly fast so a few ms difference is putting it
# all over the place. I think I'm going to keep this one for now since it gets the job done pretty well.

# Looking at the other answers, they seem pretty similar to mine just a slightly different way of thinking,
# I thought about using a hash map like other people but I thought it would be slower, I guess I was wrong
# but that's alright.

import math

class Solution:
    def isValidSudoku(self, board) -> bool:
        # Make an array with length of numbers (1-9, so length of 9)
        # Each element in that array should be another array of length of 3 (square, row, column)
        nums = [[[] for _ in range(3)] for _ in range(9)]

        # Place the square, row, column into the appropriate array. i.e 4th number, 1 square, 3 row, 2 column
        for rowNum, row in enumerate(board):
            for colNum, col in enumerate(row):
                if col != '.':
                    num = int(col)
                    squareNum = 3*math.ceil((rowNum+1)/3) + math.ceil((colNum+1)/3)
                    nums[num-1][0].append(squareNum)
                    tempHash = set(nums[num-1][0])
                    if (len(nums[num-1][0]) != len(tempHash)): return False;

                    nums[num-1][1].append(rowNum)
                    tempHash = set(nums[num-1][1])
                    if (len(nums[num-1][1]) != len(tempHash)): return False;

                    nums[num-1][2].append(colNum)
                    tempHash = set(nums[num-1][2])
                    if (len(nums[num-1][2]) != len(tempHash)): return False;

        # Check if there is a duplicate each time

        #Return true if get to end and no duplicates are found
        return True

    board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    board2 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(1, board2))