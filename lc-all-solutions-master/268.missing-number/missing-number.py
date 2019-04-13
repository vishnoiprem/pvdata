class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (n*(n+1))//2 - sum(nums)
            

nums=[9,6,4,2,3,5,7,0,1]

print(Solution().missingNumber(nums))