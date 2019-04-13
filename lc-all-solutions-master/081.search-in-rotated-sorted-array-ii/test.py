
class Solution(object):


	def search(self,nums,target):


		start=0
		end=len(nums)-1


		while start+1<end:
			mid=start+(end-start)//2


			if nums[mid]==target:
				return True

			if nums[start]<nums[mid]:

				if nums[start]<=target<=nums[mid]:
					end=mid
				else:
					start=mid

			elif nums[start]>nums[mid]:
				if nums[mid]<=target<=nums[end]:
					start=mid
				else:
					end=mid

			else:
				start+=1


		if nums[start]==target:
			return True
		elif nums[end]==target:
			return False
		return False


print (Solution().search([3, 5, 1,2], 3))
 
