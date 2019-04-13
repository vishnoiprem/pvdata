class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
                
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
                
           

# Time:  O(logn)
# Space: O(1)
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
#

class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif (nums[mid] >= nums[left] and nums[left] <= target < nums[mid]) or \
                 (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left = mid + 1

        return -1
        

if __name__ == "__main__":
    print (Solution().search([3, 5, 1], 3))
    print (Solution().search([1], 1))
    print (Solution().search([4, 5, 6, 7, 0, 1, 2], 5 ))



class Solution4(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + (r - l)) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
            
                if nums[l] <= target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
                
        return -1    



if __name__ == "__main__":
    print ('a',Solution4().search([3, 5, 1], 3))
    print (Solution4().search([1], 1))
    print (Solution4().search([4, 5, 6, 7, 0, 1, 2], 5 ))


        