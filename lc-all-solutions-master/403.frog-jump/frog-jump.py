class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp = {}
        def dfs(stones, pos, k):
            key = pos + k * 10000;
            if key in dp:
                return dp[key]
            else:
                for i in range(pos + 1, len(stones)):
                    step = stones[i] - stones[pos]
                    if step < k - 1:
                        continue;
                    if step > k + 1:
                        dp[key] = False
                        return False
                    if dfs(stones, i, step):
                        dp[key] = True
                        return True
            dp[key] = (pos == len(stones) - 1)
            return (pos == len(stones) - 1)
        return dfs(stones, 0, 0)

a=[0,1,2,3,4,8,9,11]
print(Solution().canCross(a))