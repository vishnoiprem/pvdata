class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        print('1,dp',dp)

        for i in range(1, len(s)):
            pre = int(s[i-1])
            cur = int(s[i])
            num = pre * 10 + cur
            if cur != 0:
                dp[i+1] += dp[i]
            if pre != 0 and 0 < num <= 26:
                dp[i+1] += dp[i - 1]
            
        print(dp)
        return dp[-1]
    
if __name__ == "__main__":
    for i in ["12", "27","123"]:
        print (i,Solution().numDecodings(i))