class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):

            nums[0] = nums[0]^nums[i]
            print(nums)
        return nums[0]

a=[2,2,3]

print(Solution().singleNumber(a))