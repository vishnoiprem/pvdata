class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        n -= 1

        while n > 0:

            res=""
            pre=ans[0]
            count=1

            for i in range(1,len(ans)):
                if pre==ans[i]:
                    count=count+1
                else:
                    res = res+str(count) + pre
                    pre = ans[i]
                    count = 1
            res=res+str(count)+pre
            ans=res
            n= n-1

        return ans




print(Solution().countAndSay(4))
        