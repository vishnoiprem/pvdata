class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        i = 0
        j = 0
        end = 0
        while j < len(strs) and i < len(strs[j]):
            if j == 0:
                char = strs[j][i]
            else:
                if strs[j][i] != char:
                    break
                
            if j == len(strs) - 1:
                i += 1
                j = 0
                end += 1
            else:
                j += 1

        return strs[j][:end]


    def LCP(self,str1):

        if len(str1)==0:
            return ""

        sorted_str=sorted(str1,key=lambda x:len(x))
        ans=sorted_str[0]
        #print(ans)
        i=1
        while i<len(sorted_str):
            #sorted_str[i]print(sorted_str[i])
            #print('prn',sorted_str[i].startswith(ans))
            if not sorted_str[i].startswith(ans):
                ans=ans[0:-1]
                #print(ans)
                i=0
            i=i+1
        return ans


    def LCP1(self,strs):

        if len(strs)==0:
            return ""  

        prefix = strs[0];
        print(prefix)

        for i in range(1,len(strs)):
            while not strs[i].startswith(prefix):
                prefix=prefix[0:-1]
                if  prefix =="":
                    return ""
      
        return prefix

s=Solution()
#print(s.longestCommonPrefix([ "apple", "ape", "april"]))
print(s.LCP1([ "apple", "ape", "april"]))
print(s.LCP([ "ca", "a"]))
print(s.LCP1([ "ca", "a"]))





