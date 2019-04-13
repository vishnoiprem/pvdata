class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start, nums, path, res, visited):
            res.append(path + [])
            print('start',res)
            
            for i in range(start, len(nums)):
                print(i)
                if start != i and nums[i] == nums[i - 1]:
                    continue
                if i not in visited:
                    print(i,visited)
                    visited[i] = 1
                    path.append(nums[i])
                    print('path',path)
                    dfs(i + 1, nums, path, res, visited)
                    path.pop()
                    del visited[i]
        
        nums.sort()
        res = []
        visited = {}
        dfs(0, nums, [], res, visited)
        return res
            
a=[1,2,2]

print(Solution().subsetsWithDup(a))