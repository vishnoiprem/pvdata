class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        print(nums)
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] > target:
                    end -= 1  
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    res.append((nums[i], nums[start], nums[end]))
                    end -= 1
                    start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
        return res
         
    def sum3(self,arr):
        
        d={}
        indx=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                #print(arr[i]+arr[j])
                d[(i,j)]=(arr[i]+arr[j])
                #d[(arr[i]+arr[j])]=[arr[i],arr[j]]
                indx=indx+1


        print(d)

        #print(d)

        for i in range(len(arr)):
            if -arr[i] in d.values():
                print(arr[i],'')



    def sum3_with_hash_table(self,a):
        res = []
        N = len(a)
        d = {}
        for i in range(N):
            d[a[i]] = 1

        print(d)
        a.sort()
        #rint(a)                          # O(N log N)


        # Python ranges exclude the last term, i.e., range(0,3) = [0,1,2]
        for i in range(0, N-2):           # for i = 0 to N-3
            for j in range(i+1, N-1):       # for j = i+1 to N-2
                val = -(a[i] + a[j])
                #Bprint(a[i],[j])
                if a[i] < a[j] < val and val in d:
                    #print(val)
                    #print(a[i] ,a[i] ,val,d[val])
                    res.append( [a[i], a[j], val] )
        return res

#print(Solution)

    def sum3_num(self,nums):

        n=len(nums)
        res=set()
        nums.sort()
        print(nums)


        if n<3:
            return []

        for i in range(n-2):

            if i==0 or nums[i]!=nums[i-1]:
                j=i+1
                k=n-1


                while j<k:
                    sum=nums[i]+nums[j]+nums[k]
                    print(i,nums[i],nums[j],nums[k])

                    if sum==0:
                        res.add((nums[i],nums[j],nums[k]))
                        j=j+1
                        k=k-1
                    elif sum<0:
                        j=j+1
                    else:
                        k=k-1

        return list(res)




a=[-1, 0, 1, 2, -1, -4]
s =Solution()
#print(s.threeSum([-1, 0, 1, 2, -1, -4]))
#print(s.sum3([-1, 0, 1, 2, -1, -4]))
print(s.sum3_with_hash_table([-1, 0, 1, 2, -1, -4]))
#


