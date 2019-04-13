class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        preSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            print(preSum,maxSum,i)
            preSum = max(preSum + nums[i], nums[i])
            maxSum = max(maxSum, preSum)
        return maxSum


if __name__ == "__main__":
    print (Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))