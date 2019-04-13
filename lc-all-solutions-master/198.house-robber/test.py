class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for i in range(0, 2)]

        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        print(dp)
        for i in range(2, len(nums)):
            dp[i%2] = max(dp[(i - 1)%2], dp[(i - 2)%2] + nums[i])
            print(dp,nums[:i+1])

        print(dp)
        return dp[(len(nums) - 1)%2]



if __name__ == '__main__':
        print (Solution().rob([8,4,8,5,9,6,5,4,4,10]))
        print (Solution().rob([8,4,8]))
