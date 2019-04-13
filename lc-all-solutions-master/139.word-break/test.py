class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        max_len = 0
        for string in wordDict:
            max_len = max(max_len, len(string))
        print(max_len)

        can_break = [False for _ in range(n + 1)]
        print(can_break)

        can_break[0] = True

        for i in range(1, n + 1):
            for l in range(1, min(i, max_len) + 1):
                print(i,l,can_break[i-l] and s[i-l:i] in wordDict,s[i-l] , can_break[i-l],s[i-l:i] ,'--', wordDict)
                if can_break[i-l] and s[i-l:i] in wordDict:
                    can_break[i] = True
                    break
        return can_break[-1]

    
if __name__ == "__main__":
    print (Solution().wordBreak("leetcode", ["leet", "code"]))