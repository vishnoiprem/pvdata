
class Solution(object):


	def missingNumber(self, nums):


		nums=sorted(nums)
		count=nums[0]
		i=0

		fount=False
		while i<len(nums) and not fount:


			if nums[i]!=count:
				fount=True
				return count

			count=count+1
			i=i+1




nums=[9,6,4,2,3,5,7,0,1]

print(Solution().missingNumber(nums))