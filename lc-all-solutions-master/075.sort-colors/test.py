

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        start=0
        end=len(nums)-1



        def swap(a,b):
        	temp=nums[b]
        	nums[b]=nums[a]
        	nums[a]=temp

        for i in range(len(nums)):


        	while nums[i]==2 and i<end:
        		swap(i,end)
        		end=end-1
        	while nums[i]==0 and i>start:
        		swap(i,start)
        		start=start+1


a = [2,0,0,0,1,1,1,0,0,0,2,1,0,0]
res = Solution().sortColors(a)
print (a)


