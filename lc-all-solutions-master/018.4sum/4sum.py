import collections 

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in xrange(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if sum < target:
                        start += 1
                    elif sum > target:
                        end -= 1
                    else:
                        res.append((nums[i], nums[j], nums[start], nums[end]))
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
        return res



class Solution1(object):

    """
    input: list[int], int
    output: list[]
    """

    def fourSum(self,nums,target):
        #print(nums,target)
        dict=collections.defaultdict(set)
        #print(dict)
        n=len(nums)
        nums.sort()

        if n<4:
            return []
        res=set()

        for i in range(n-1):
            for j in range(i+1,n):
                #print(i,j)
                sum=nums[i]+nums[j]
                print('sum',sum)
                for sub in dict[target-sum]:
                    print('sub',sub,dict)
                    res.add(tuple(list(sub)+[nums[i],nums[j]]))

                for j in range(i):
                    dict[nums[i]+nums[j]].add((nums[j],nums[i]))

        return list(res)






s=Solution1()
print(s.fourSum([1, 0, -1, 0, -2, 2],0))


