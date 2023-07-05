# Version 1 is complete and accepted by leetcode. Not very fast but great on memory, used 16.1mb beating 98.1% of submissions. Running multiple times get
# all over the place, the speed can go up to 80% but also down to 20%, same thing with memory but will go up to 98.1%

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if numRows == 1 or length <= numRows or length <= 2:
            return s
        row = 1
        col = 1
        solution = ""
        prev = None
        for i in range(length + numRows):
            if col == 1:
                prev = row
            elif row == 1 or row == numRows:
                prev = ((numRows - 1)*2) + prev
            else:
                if col % 2 == 0:
                    prev = ((numRows - row)*2) + prev
                else:
                    prev = ((row - 1)*2) + prev
            if prev > length:
                row += 1
                col = 1
            else:
                col += 1
                solution += s[prev-1]
        return solution

    tests = [["SOLUTION", 3, "STOUINLO"], ["PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"], ["A", 1, "A"]]

    for test in tests:
        print(test[2] == convert(1, test[0], test[1]))