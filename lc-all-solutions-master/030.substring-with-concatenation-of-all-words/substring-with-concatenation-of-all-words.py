from collections import deque
import collections 
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) > len(s):
            return []
        d = {}
        t = {}
        ans = []
        deq = deque([])
        wl = len(words[0])
        fullscore = 0
        for word in words:
            d[word] = d.get(word, 0) + 1
            fullscore += 1
        print(d)
            
        for i in range(0, len(s)):
            head = start = i
            t.clear()
            score = 0
            
            while start + wl <= len(s) and s[start:start + wl] in d:
                cword = s[start:start + wl]
                t[cword] = t.get(cword, 0) + 1
                if t[cword] <= d[cword]:
                    score += 1
                else:
                    break
                start += wl

                
            if score == fullscore:
                ans.append(head)
        
        return ans
                
                 
if __name__ == "__main__":
    print (Solution().findSubstring("barfoothefoobarman", ["foo", "bar","bar"]))


# Time:  O(m * n * k), where m is string length, n is dictionary size, k is word length
# Space: O(n * k)
class Solution2(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result, m, n, k = [], len(s), len(words), len(words[0])
        if m < n*k:
            return result
 
        lookup = collections.defaultdict(int)
        print(lookup)
        for i in words:
            lookup[i] += 1 
                                   # Space: O(n * k)

        print(lookup)
        for i in range(m+1-k*n):                     # Time: O(m)
            cur, j = collections.defaultdict(int), 0
            while j < n:                              # Time: O(n)
                word = s[i+j*k:i+j*k+k]               # Time: O(k)
                print(word)
                if word not in lookup: 
                    break
                cur[word] += 1
                if cur[word] > lookup[word]:
                    break
                j += 1
            if j == n:
                result.append(i)
                
        return result


if __name__ == "__main__":
    print (Solution2().findSubstring("barfoothefoobarman", ["foo", "bar"]))