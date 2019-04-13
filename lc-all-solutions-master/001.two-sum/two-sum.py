class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                print(target-num)
                return [d[target - num], i]
            d[num] = i
            print(d)
        # no special case handling becasue it's assumed that it has only one solution
nums = [2,45,7,3,5,1,8,9]
target = 10  

print(Solution().twoSum(nums,target))



def sum2(a,target):
    d={}
    len_a=len(a)


    for i,n in enumerate(nums):

        diff= target-a[i]
        #print(diff)
        if diff in d:
            print(d[target - n],i)
        #print(diff,a[i])
        d[i]=a[i]

        #print(d)





print(sum2(nums,target))


nums = [2,45,7,3,5,1,8,9]
target = 10 


def sumTwo(nums,target):
    d={}

    for i in range(len(nums)):

        if target-nums[i] in d:
            return i,d[target-nums[i]]


        d[nums[i]]=i

        #print(d)


print(sumTwo(nums,target))


