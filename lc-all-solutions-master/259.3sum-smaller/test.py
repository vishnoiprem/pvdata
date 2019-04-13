



def threeSumSmaller(nums,target):

	ans=0
	nums.sort()
	#nlogn
	print(nums)

	for i in range(0,len(nums)):
		start,end=i+1,len(nums)-1
		while start<end:

			if nums[i]+nums[start]+nums[end]<target:
				ans=ans+end-start
				start=start+1
			else:
				end=end-1
	return ans


nums = [-2, 0, 1, 3]
target = 2



print(threeSumSmaller(nums,target))