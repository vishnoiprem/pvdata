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
                print(s,'s')
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


if __name__ == "__main__":
    print (Solution().longestConsecutive([100, 4, 200, 1, 3, 2, 2]))


