class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(nums, target, path, res):
            if target == 0:
                res.append(path + [])
                return
            
            for i in range(0, len(nums)):
                if path and nums[i] < path[-1]:
                    continue
                if target - nums[i] < 0:
                    return
                path.append(nums[i])
                dfs(nums, target - nums[i], path, res)
                path.pop()
        candidates.sort()
        res = []
        dfs(candidates, target, [], res)
        return res


arr=[2, 3, 6, 7] 
target=7


print(Solution().combinationSum(arr,target))