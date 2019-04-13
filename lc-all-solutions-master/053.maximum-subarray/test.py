class Solution:


	def maxSubArray(self,arr):
		print(arr)


		preSum=arr[0]
		maxSum=arr[0]

		for j in range(1,len(arr)):
			preSum=max(preSum+arr[j],arr[j])
			maxSum=max(preSum,maxSum)

		return maxSum




if __name__ == "__main__":
    print (Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))