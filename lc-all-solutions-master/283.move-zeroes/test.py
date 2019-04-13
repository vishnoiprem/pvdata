class Solution(object):


	def moveZeros(self, nums):


		i=0
		j=0

		for i in range(0,len(nums)):

			if nums[i]!=0:
				nums[j],nums[i]=nums[i],nums[j]
				j=j+1
		return nums


if __name__=="__main__":
	print(Solution().moveZeros([1,2,3,0,1,0]))