
import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) in [0,1,2]:
            return 0
        else:
            min_diff = sys.maxsize
            print(min_diff)
            result = 0
            sorted_nums = sorted(nums)
            for i in range(len(nums)):
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    curr_sum = sorted_nums[i] + sorted_nums[start] + sorted_nums[end]
                    diff = abs(curr_sum - target)
                    if diff == 0:
                        return curr_sum
                    if diff < min_diff:
                        print(diff,curr_sum)
                        min_diff = diff
                        result = curr_sum
                    if curr_sum <= target:
                        start += 1
                    else:
                        end -= 1
            return result
if __name__ == "__main__":
    soln = Solution()
    print(soln.threeSumClosest([-1, 2, 1, -4], 1))
    print(soln.threeSumClosest([-1, 2, 1, -4], 3))