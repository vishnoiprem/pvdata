class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        x = y = z = -1
        for i in range(0, len(nums)):
            if nums[i] == 0:
                x += 1
                y += 1
                z += 1
                if z != -1:
                    nums[z] = 2
                if y != -1:
                    nums[y] = 1
                nums[x] = 0
            elif nums[i] == 1:
                y += 1
                z += 1
                nums[z] = 2
                if x != -1:
                    nums[x] = 0
                if y != -1:
                    nums[y] = 1
            elif nums[i] == 2:
                z += 1
                if y != -1:
                    nums[y] = 1
                if x != -1:
                    nums[x] = 0
                nums[z] = 2

if __name__ == "__main__":
    A = [2, 1, 1, 0, 0, 2]
    Solution().sortColors(A)
    print (A)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def swap(i,j):
            temp=nums[i]

            nums[i], nums[j] = nums[j], temp
            print(nums,i,j)


        l = len(nums)

        left, right = 0, len(nums) - 1 

        for i in range(l):

            while nums[i] == 2 and i < right:
                swap(i,right)
                right -= 1

            while nums[i] == 0 and i > left:
                swap(i,left)
                left += 1 

r = Solution()

a = [2,0,0,0,1,1,1,0,0,0,2,1,0,0]
res = r.sortColors(a)
print (a)