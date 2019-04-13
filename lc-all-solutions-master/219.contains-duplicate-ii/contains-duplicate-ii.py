from collections import deque
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        if k == 0:
            return False
        k = k + 1
        k = min(k, len(nums))

        window = deque([])
        d = set()
        for i in range(0, k):
            if nums[i] in d:
                return True
            d |= {nums[i]}
            window.append(i)
        for i in range(k, len(nums)):
            d -= {nums[window.popleft()]}
            if nums[i] in d:
                return True
            d |= {nums[i]}
            window.append(i)
        return False
            
# Time:  O(n)
# Space: O(n)
#
# Given an array of integers and an integer k, return true if 
# and only if there are two distinct indices i and j in the array 
# such that nums[i] = nums[j] and the difference between i and j is at most k.
#

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = i
            else:
                # It the value occurs before, check the difference.
                if i - lookup[num] <= k:
                    return True
                # Update the index of the value.
                lookup[num] = i
        return False

nums=[1,1,4,3]
k=3
print(Solution().containsNearbyDuplicate(nums,k))