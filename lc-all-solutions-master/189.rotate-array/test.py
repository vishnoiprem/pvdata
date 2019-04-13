


class Solution(object):

	def rotate(self, numarr, k=0):

		if len(numarr) == 0 or k == 0:
			return

		for i in range(k):

			numarr.insert(0,numarr[-1])
			numarr.pop()
		#print(numarr)

	def rotate2(self, nums, k):


		nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
		print(nums)


print(Solution().rotate2([1,2,3,4,5,6,7],3))