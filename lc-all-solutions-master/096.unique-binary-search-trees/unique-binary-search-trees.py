class Solution(object):
    def _numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        print(dp)

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                print('dp',dp[i],dp[j - 1] * dp[i - j])
                dp[i] = dp[i]+dp[j - 1] * dp[i - j]
            print(dp)
        return dp[-1]
        
    def numTrees(self, n):
        ans = 1
        for i in range(1, n + 1):
            print(i)
            ans = ans * (n + i) // i
        return ans // (n + 1)
            

print(Solution()._numTrees(5))
            
# Time:  O(n)
# Space: O(1)
#
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
# 
# For example,
# Given n = 3, there are a total of 5 unique BST's.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#

# Math solution.
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        def combination(n, k):
            count = 1
            # C(n, k) = (n) / 1 * (n - 1) / 2 ... * (n - k + 1) / k
            for i in range(1, k + 1):
                count = count * (n - i + 1) / i;
            return count

        return combination(2 * n, n) - combination(2 * n, n - 1)

# Time:  O(n^2)
# Space: O(n)
# DP solution.
class Solution2:
    # @return an integer
    def numTrees(self, n):
        counts = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for j in range(i):
                count += counts[j] * counts[i - j - 1]
            counts.append(count)
        return counts[-1]
    
if __name__ == "__main__":
    print (Solution2().numTrees(3))