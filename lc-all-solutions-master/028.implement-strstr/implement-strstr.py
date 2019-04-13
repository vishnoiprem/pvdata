class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
                
        for i in range(0, len(haystack)):
            k = i
            j = 0
            while j < len(needle) and k < len(haystack) and haystack[k] == needle[j]:
                j += 1
                k += 1
            if j == len(needle):
                return i
        return -1 if needle else 0
            
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


if __name__ == "__main__":
    #print (Solution().strStr("a", ""))
    print (Solution().strStr("abababcdab", "ababcdx"))





















class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        print('sol',len(haystack) - len(needle) + 1)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                print(haystack[i : i + len(needle)])
                return i
        return -1
    
if __name__ == "__main__":
    print (Solution2().strStr("ab", "b"))
    print (Solution2().strStr("abababcdab", "ababcdx"))
    print (Solution2().strStr("aabababa", "ababab"))
