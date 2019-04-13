
# Time:  O(m * n)
# Space: O(m + n)
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# 
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# 
# How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
#


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        print(dp)

        for i in range(1, m):
            pre = 1
            for j in range(1, n):
                dp[j] = dp[j] + pre
                pre = dp[j]
                print(dp,i,j)
        return dp[-1]

if __name__ == "__main__":
    print (Solution().uniquePaths(3, 7))