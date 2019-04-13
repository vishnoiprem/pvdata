class Solution(object):
    def majorityElement(self, num):
        return sorted(num)[len(num)//2]



print(Solution().majorityElement([1,2,3,4]))