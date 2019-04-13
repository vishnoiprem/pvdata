class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}

        for i in range(len(nums)):
            if target-nums[i] in d:
                return [i,d[target-nums[i]]]
            d[nums[i]]=i
        return []



nums = [2,45,7,3,5,1,8,9]
target = 10  

print(Solution().twoSum(nums,target))


