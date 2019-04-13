class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        s = set(nums)
        print(s)
        for num in nums:
            if num in s:
                s.discard(num)
                print(s)
                cnt = 1
                right = num + 1
                left = num - 1
                while left in s:
                    s.discard(left)
                    cnt += 1
                    left -= 1
                while right in s:
                    s.discard(right)
                    cnt += 1
                    right += 1
                ans = max(ans, cnt)
        return ans

a=[100, 4, 200, 1, 3, 2]
#print(Solution().longestConsecutive(a))


# Time:  O(n)
# Space: O(n)
#
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# 
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# 
# Your algorithm should run in O(n) complexity.
#

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        result, lengths = 1, {key: 0 for key in num}
        print(lengths.get(100,3))
        print(result,lengths)
        for i in num:
            if lengths[i] == 0:
                lengths[i] = 1
                left, right = lengths.get(i - 1, 0), lengths.get(i + 1, 0)
                print(left,right)
                length = 1 + left + right
                result, lengths[i - left], lengths[i + right] = max(result, length), length, length
        return result

if __name__ == "__main__":
    print (Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))