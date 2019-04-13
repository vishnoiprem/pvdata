class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = -1
        for i in range(0, len(nums)):

            if nums[i] != val:
                print(i)
                slow = slow+1
                nums[slow] = nums[i]
        print(nums)
        return slow + 1
                



print(Solution().removeElement([1,9,7],1))
