from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        nrows = len(matrix)
        ncols = len(matrix[0])
        max_square_len = 0
        dp = [[0] * (ncols + 1) for i in range(nrows + 1)]
        print(dp)
        
        for i in range(1, nrows + 1):
            for j in range(1, ncols + 1):
                if (matrix[i - 1][j - 1] == '1'):
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    max_square_len = max(max_square_len, dp[i][j])
                    
        return max_square_len ** 2


s = Solution()
result = s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
if result != 4:
    print ("Error 1. 4 != %d" % result)
else :
    print ("Pass 1")

result = s.maximalSquare([["0","1"],["1","0"]])
if result != 1:
    print ("Error 2. 1 != %d" % result)
else :
    print ("Pass 2")

result = s.maximalSquare([["0"]])
if result != 0:
    print ("Error 3. 0 != %d" % result)
else :
    print ("Pass 3")

result = s.maximalSquare([["0","1","1","0","0","1","0","1","0","1"],["0","0","1","0","1","0","1","0","1","0"],["1","0","0","0","0","1","0","1","1","0"],["0","1","1","1","1","1","1","0","1","0"],["0","0","1","1","1","1","1","1","1","0"],["1","1","0","1","0","1","1","1","1","0"],["0","0","0","1","1","0","0","0","1","0"],["1","1","0","1","1","0","0","1","1","1"],["0","1","0","1","1","0","1","0","1","1"]])
if result != 4:
    print ("Error 4. 4 != %d" % result)
else :
    print ("Pass 4")
