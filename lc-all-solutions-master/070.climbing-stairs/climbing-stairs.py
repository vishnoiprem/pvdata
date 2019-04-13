class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        pre, ppre = 1, 1
        for i in range(2, n + 1):
            tmp = pre
            pre = ppre + pre
            ppre = tmp
        return pre

# Time:  O(n)
# Space: O(1)
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?


class Solution:
    """
    :type n: int
    :rtype: int
    """
    def climbStairs(self, n):
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current, 
        return current

    # Time:  O(2^n)
    # Space: O(n)
    def climbStairs1(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

if __name__ == "__main__":
    result = Solution().climbStairs(4)
    print (result)