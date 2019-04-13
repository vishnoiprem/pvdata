import bisect
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k == 0:
            return False
        bst = []
        if k < 0 or t < 0:
            return False
        for i, num in enumerate(nums):
            idx = bisect.bisect_left(bst, num)    
            if idx < len(bst) and abs(bst[idx] - num) <= t:
                return True
            if idx > 0 and abs(bst[idx - 1] - num) <= t:
                return True
            if len(bst) >= k:
                del bst[bisect.bisect_left(bst, nums[i - k])]
            bisect.insort(bst, num)
        return False
        
        


# Time:  O(n * t)
# Space: O(max(k, t))
#
# Given an array of integers, find out whether there 
# are two distinct inwindowes i and j in the array such 
# that the difference between nums[i] and nums[j] is 
# at most t and the difference between i and j is at 
# most k.
#

# This is not the best solution 
# since there is no built-in bst structure in Python.
# The better solution could be found in C++ solution.
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for n in nums:
            # Make sure window size
            if len(window) > k:
                window.popitem(False)
                
            bucket = n if not t else n // t
            # At most 2t items.
            for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            window[bucket] = n
        return False