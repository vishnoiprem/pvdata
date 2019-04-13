class Solution(object):
   
    def sum3_with_hash_table(self,a):
        
        res = []
        
        N = len(a)
        
        d = {}

        for i in range(N):
            d[a[i]] = 1
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

a=[-1, 0, 1, 2, -1, -4]
s =Solution()
#print(s.threeSum([-1, 0, 1, 2, -1, -4]))
#print(s.sum3([-1, 0, 1, 2, -1, -4]))
#print(s.sum3_with_hash_table([-1, 0, 1, 2, -1, -4]))
print('so',Solution().sum3_with_hash_table(a))


"""


S = [-1, 0, 1, 2, -1, -4]
print(s)

n=len(S)
print(n)
d={}

for i,c in enumerate(S):
    print(i,c)
    d[c]=1

print(d)

set1=set()
S.sort()

for i in range(n-1):
    for j in range(i+1,n):
        if S[i]<S[j]<(S[i]+S[j])  and -(S[i]+S[j]) in d:
            sum1=(-(S[i]+S[j]),S[i],S[j])
            print(set1.add(sum1))

print(set1)

"""

