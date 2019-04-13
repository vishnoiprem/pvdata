class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        n = len(s)
        def isValid(num):
            print(num)
            if len(num) == 1:
                return True
            if len(num) > 1 and num[0] != "0" and int(num) <= 255:
                return True
            return False
            
        for i in range(0, min(3, n - 3)):
            a = s[:i+1]
            print(a)
            if not isValid(a):
                break
            for j in range(i + 1, min(i + 4, n - 2)):
                b = s[i+1:j+1]
                if not isValid(b):
                    break
                for k in range(j + 1, min(j + 4, n - 1)):
                    c = s[j+1:k+1]
                    d = s[k+1:]
                    if not isValid(c):
                        break
                    if not isValid(d):
                        continue
                    ans.append("{}.{}.{}.{}".format(a, b, c, d))
        return ans
    
if __name__ == "__main__":
    print (Solution().restoreIpAddresses("25525511135"))

# Time:  O(n^m) = O(3^4)
# Space: O(n * m) = O(3 * 4)
#
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# 
# For example:
# Given "25525511135",
# 
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        result = []
        self.restoreIpAddressesRecur(result, s, 0, "", 0)
        return result
        
    def restoreIpAddressesRecur(self, result, s, start, current, dots):
        # pruning to improve performance
        if (4 - dots) * 3 < len(s) - start or (4 - dots) > len(s) - start:
            return
        
        if start == len(s) and dots == 4:
            result.append(current[:-1])
        else:
            for i in range(start, start + 3):
                if len(s) > i and self.isValid(s[start:i + 1]):
                    current += s[start:i + 1] + '.'
                    self.restoreIpAddressesRecur(result, s, i + 1, current, dots + 1)
                    current = current[:-(i - start + 2)]
        
    def isValid(self, s):
        if len(s) == 0 or (s[0] == '0' and s != "0"):
            return False
        return int(s) < 256
    
if __name__ == "__main__":
    print ('Upper One',Solution().restoreIpAddresses("0000"))


class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        def dfs(s, sub, ips, ip):
            if sub == 4:                                        # should be 4 parts
                if s == '':
                    ips.append(ip[1:])                          # remove first '.'
                    print(ips)
                return
            for i in range(1, 4):                               # the three ifs' order cannot be changed!
                if i <= len(s):                                 # if i > len(s), s[:i] will make false!!!!
                    if int(s[:i]) <= 255:
                        print(s[:i])
                        dfs(s[i:], sub+1, ips, ip+'.'+s[:i])
                    if s[0] == '0': break                       # make sure that res just can be '0.0.0.0' and remove like '00'
        ips = []
        dfs(s, 0, ips, '')
        return ips

    
if __name__ == "__main__":
    print (Solution().restoreIpAddresses("25525519135"))

