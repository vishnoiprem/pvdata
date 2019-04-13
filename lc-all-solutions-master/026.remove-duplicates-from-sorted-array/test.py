def removeDuplicates(nums):

	i=0
	n=len(nums)

	while i<=n-2:
		print(nums)

		if nums[i]==nums[i+1]:
			nums[i]=nums[i+1]
			nums.pop(i+1)
			n=len(nums)
			if not i>n:
				i=i+1

		else:
			i=i+1
	return nums


def removeDuplicates1(nums):

	i=1

	while i<len(nums):

		if nums[i-1]!=nums[i]:
			i=i+1
		else:
			nums.pop(i)
			i=i
			print(i,nums)

	return nums








print(removeDuplicates1([2,2,2,2,2]))
