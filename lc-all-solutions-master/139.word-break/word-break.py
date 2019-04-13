class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        queue = [0]
        ls = len(s)
        lenList = [l for l in set(map(len, wordDict))]
        visited = [0 for _ in range(0, ls + 1)]
        while queue:
            start = queue.pop(0)
            for l in lenList:
                if s[start:start + l] in wordDict:
                    if start + l == ls:
                        return True
                    if visited[start + l] == 0:
                        queue.append(start + l)
                        visited[start + l] = 1
        return False







# Time:  O(n * l^2)
# Space: O(n)

# Given a string s and a dictionary of words dict, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# 
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# 
# Return true because "leetcode" can be segmented as "leet code".

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        print('l'   in wordDict)

        max_len = 0
        print(n)
        for string in wordDict:
            max_len = max(max_len, len(string))
            print(max_len)

        can_break = [False for _ in range(n + 1)]
        print(can_break)

        can_break[0] = True

        for i in range(1, n + 1):
            for l in range(1, min(i, max_len) + 1):
                print(i,l,can_break[i-l] and s[i-l:i] in wordDict,can_break[i-l] , s[i-l:i] , wordDict)
                if can_break[i-l] and s[i-l:i] in wordDict:
                    can_break[i] = True
                    break
        print(can_break)
        return can_break[-1]

    
if __name__ == "__main__":
    print (Solution().wordBreak("leetcode", ["leet", "code"]))