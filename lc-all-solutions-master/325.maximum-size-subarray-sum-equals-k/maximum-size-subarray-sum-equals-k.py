class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0: -1}
        maxLen = 0
        _sum = 0
        for i in xrange(0, len(nums)):
            _sum += nums[i]
            if _sum not in d:
                d[_sum] = i
            if _sum - k in d:
                maxLen = max(maxLen, i - d[_sum - k])
        return maxLen


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        seen = {}
        acc = 0
        res = float("-inf")
        for i, num in enumerate(nums):
            acc = acc+num
            print(acc)

            if num not in seen:

                seen[acc] = i
                print(acc,seen,i)
            elif acc - k in seen:
                print(i,seen[acc -k])
                res = max(res, i - seen[acc -k])

        return res




r = Solution()

res = r.maxSubArrayLen([1,-1,5,-2,3], 3)

print (res)
