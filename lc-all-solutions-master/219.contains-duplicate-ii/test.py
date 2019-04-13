def containDuplicate(nums,k):

	d={}

	for i,n in enumerate(nums):
		if n not in d:
			print("Yes")
			d[n]=i
		else:
			if i-d[n]<=k:
				return True
			d[n]=i
		print(d)



nums=[1,1,4,3]
k=3
print(containDuplicate(nums,k))