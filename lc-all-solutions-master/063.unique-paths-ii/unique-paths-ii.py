# Time:  O(m * n)
# Space: O(m + n)
#
# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# 
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
# 
# Note: m and n will be at most 100.
#















class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        if grid[0][0] == 1:
            return 0
        dp = [[0] * len(grid[0]) for _ in range(0 ,len(grid))]
        dp[0][0] = 1 if grid[0][0] == 0 else 0
        for i in range(1, len(grid)):
            if grid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        
        for j in range(1, len(grid[0])):
            if grid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == "__main__":
    obstacleGrid = [
                      [0,0,0],
                      [0,1,0],
                      [0,0,0]
                   ]
    print (Solution().uniquePathsWithObstacles(obstacleGrid))
        