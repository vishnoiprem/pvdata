# Time:  O(n)
# Space: O(1)
#
# Given a sorted integer array without duplicates,
# return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7],
# return ["0->2","4->5","7"].
#
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        ranges = []
        if not nums:
            return ranges

        start, end = nums[0], nums[0]

        for i in range(1, len(nums) + 1):

            if i < len(nums) and nums[i] == end + 1:
                end = nums[i]
            else:
                interval = str(start)
                if start != end:
                    interval += "->" + str(end)
                ranges.append(interval)
                if i < len(nums):
                    start = end = nums[i]
        return ranges

print(Solution().summaryRanges([0,1,2,4,5,7]))
