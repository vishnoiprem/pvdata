class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end, mid = 0, len(nums) - 1, 0

        
        print(start,end,mid)
        while start + 1 < end:
            mid = start + (end - start) // 2
            print('mid',mid,'start',nums[start],'mid',nums[mid])
            if nums[start] <= nums[mid]:
                start = mid
            else:
                end = mid
        return min(nums[0], nums[start], nums[end])

a=[4,5,6,7,1,2]

print(Solution().findMin(a))