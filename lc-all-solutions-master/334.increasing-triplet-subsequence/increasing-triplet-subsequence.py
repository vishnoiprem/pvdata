class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = b = float("inf")
        for num in nums:
            print(num)
            if num <=a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False

#a=[1, 2, 3, 4, 5],
#print(Solution().increasingTriplet(a))


# Time:  O(n)
# Space: O(1)

# Given an unsorted array return whether an increasing 
# subsequence of length 3 exists or not in the array.

# Formally the function should:
# Return true if there exists i, j, k 
# such that arr[i] < arr[j] < arr[k] 
# given 0 <= i < j < k <= n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Examples:
# Given [1, 2, 3, 4, 5],
# return true.

# Given [5, 4, 3, 2, 1],
# return false.


class Solution2(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_num, a, b = float("inf"), float("inf"), float("inf")
        for c in nums:
            print(min_num,a,b)
            if min_num >= c:
                min_num = c
            elif b >= c:
                a, b = min_num, c
            else:  # a < b < c
                return True
        return False
a=[7, 1, 5, 3, 5]
a=[5, 4, 3, 2, 1]
print(Solution2().increasingTriplet(a))
