class Solution(object):
    # better way
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] * nums[i - 1]
            print(dp,i,dp[i - 1] , nums[i - 1])
        prod = 1
        for i in reversed(range(0, len(nums))):
            print(i)
            dp[i] = dp[i] * prod
            prod = prod*nums[i]
            print(dp)
        return dp


print(Solution().productExceptSelf([1,2,3,4]))