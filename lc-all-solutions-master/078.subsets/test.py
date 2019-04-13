class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        
        result = [[]]
        
        for i in range(len(nums)):
            
            size = len(result)
            
            for j in range(size):
                result.append(list(result[j]))
                print('before last',result,i,j)
                result[-1].append(nums[i])
                print('after ',result)
        return result
print(Solution().subsets([1,2,3]))