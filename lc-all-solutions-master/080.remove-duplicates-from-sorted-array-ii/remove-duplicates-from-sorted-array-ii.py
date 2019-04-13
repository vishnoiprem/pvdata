class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        cnt = 0
        j = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                cnt += 1
                if cnt < 2:
                    nums[j] = nums[i]
                    j += 1
            else:
                nums[j] = nums[i]
                j += 1
                cnt = 0
        return j


print(Solution().removeDuplicates([1,2]))


class Solution(object):

    def mark(self, nums):
        print(nums)

        prev = nums[0]
        prevCounter = 1

        for index, num in enumerate(nums[1:]):

            if num == prev:

                if prevCounter == 2:
                    nums[index + 1] = None
                else:
                    prevCounter += 1
            else:
                prevCounter = 1

            prev = num

        return nums


    def next_dup(self, nums, i):

        for idx in range(i, len(nums)):

            if nums[idx]:
                return idx

    def removeDuplicates(self, nums):

        if nums == []:
            return

        nums = self.mark(nums)

        l = len([x for x in nums if x is not None])

        i = -1

        print (nums)
        for idx, num in enumerate(nums):

            if num is None:
                if i == -1:
                    i = idx
            else:
                if i != -1:
                    nums[i] = num
                    nums[idx] = None
                    i += 1
        print (nums)
        return l



r = Solution()
res = r.removeDuplicates([0,0,0,0,0,1,2,2,3,3,4,4,4, 5,5,5,5,5])
#res = r.removeDuplicates([1,1,1,2,2,3])

#print (res)


# Time:  O(n)
# Space: O(1)
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# For example,
# Given sorted array A = [1,1,1,2,2,3],
# 
# Your function should return length = 5, and A is now [1,1,2,2,3].
#

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        
        last, i, same = 0, 1, False

        while i < len(A):
            if A[last] != A[i] or not same:
                same = A[last] == A[i]
                last += 1
                A[last] = A[i]
            i = i+1
            
        return last + 1

if __name__ == "__main__":
    print (Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)<=2:
            return 0
        count=0
        for i in range(1,len(A)):
            if A[i]==A[i-1]:
                count=count+1

                #print('cnt',count)

        return count+1

if __name__ == "__main__":
    print (Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))




