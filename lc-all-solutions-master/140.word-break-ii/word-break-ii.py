class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        res = []
        if not self.checkWordBreak(s, wordDict):
            return res
        queue = [(0, "")]
        slen = len(s)
        lenList = [l for l in set(map(len, wordDict))]
        while queue:
            tmpqueue = []
            for q in queue:
                start, path = q
                for l in lenList:
                    if start + l <= slen and s[start:start+l] in wordDict:
                        newnode = (start + l, path + " " + s[start:start+l] if path else s[start:start+l])
                        tmpqueue.append(newnode)
                        if start + l == slen:
                            res.append(newnode[1])
            queue, tmpqueue = tmpqueue, []
        return res

    def checkWordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        queue = [0]
        slen = len(s)
        lenList = [l for l in set(map(len,wordDict))]
        visited = [0 for _ in range(0, slen + 1)]
        while queue:
            tmpqueue = []
            for start in queue:
                for l in lenList:
                    if s[start:start+l] in wordDict:
                        if start + l == slen:
                            return True
                        if visited[start + l] == 0:
                            tmpqueue.append(start+l)
                            visited[start + l] = 1
            queue, tmpqueue = tmpqueue, []
        return False


# Time:  O(n * l^2 + n * r), l is the max length of the words, 
#                            r is the number of the results.
# Space: O(n^2)
#
# Given a string s and a dictionary of words dict, 
# add spaces in s to construct a sentence where each word is a valid dictionary word.
# 
# Return all such possible sentences.
# 
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
# 
# A solution is ["cats and dog", "cat sand dog"].
#

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        n = len(s)

        max_len = 0
        for string in wordDict:
            max_len = max(max_len, len(string))

        can_break = [False for _ in range(n + 1)]
        valid = [[False] * n for _ in range(n)]
        print(len(valid[0]))
        can_break[0] = True
        for i in range(1, n + 1):
            for l in range(1, min(i, max_len) + 1):
                if can_break[i-l] and s[i-l:i] in wordDict:
                    valid[i-l][i-1] = True
                    can_break[i] = True

        result = []
        print(valid)
        if can_break[-1]:
            self.wordBreakHelper(s, valid, 0, [], result)
        return result
    
    def wordBreakHelper(self, s, valid, start, path, result):
        if start == len(s):
            result.append(" ".join(path))
            return
        for i in range(start, len(s)):
            if valid[start][i]:
                path += [s[start:i+1]]
                self.wordBreakHelper(s, valid, i + 1, path, result)
                path.pop()


if __name__ == "__main__":
    print (Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))

    print(list(zip('egg','add')))