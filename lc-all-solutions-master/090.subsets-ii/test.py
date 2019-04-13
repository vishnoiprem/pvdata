class Solution(object):


	def subsetsWithDup(self,nums):

	
		def dfs(start, nums, path, res, visited):
			print('path',path,res)

			res.append(path+[])


			for i in range(start,len(nums)):
				print(i,visited,'i')

				if start!=i and nums[i] == nums[i - 1]:

					continue 
				if i is not visited:

					visited[i]=1
					print('inner ', i,visited)

					path.append(nums[i])
					dfs(i + 1, nums, path, res, visited)
					path.pop()

		nums.sort()
		visited={}
		res=[]

		dfs(0, nums, [], res, visited)
		return res



a=[1,2]

print(Solution().subsetsWithDup(a))