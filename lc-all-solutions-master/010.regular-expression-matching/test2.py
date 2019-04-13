class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        dp=[ [ False]*(len(p)+1) for i in range(len(s)+1)]
        dp[0][0]=True



        for i in range(1,len(p)+1):

            if p[i-1]=="*":
                dp[0][i]=dp[0][i-2]

        print(dp)


        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):


                if p[j-1]!="*":
                    dp[i][j] = dp[i-1][j-1] and (s[i -1] == p[j - 1] or p[j - 1] == ".")
                else:
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == ".")
        return dp[-1][-1]











s=Solution()
#print(s.isMatch("a",""))

#print(s.isMatch("xaabyc","xa*b.c"))
print(s.isMatch('ababab','a*'))

#print(s.isMatch("aa","a"))
#print(s.isMatch("aa","aa"))
#print(s.isMatch("aaa","aa"))
#print(s.isMatch("aa", "a*"))
#print(s.isMatch("aa", ".*"))
#print(s.isMatch("ab", ".*"))
#print(s.isMatch("aab", "c*a*b") )