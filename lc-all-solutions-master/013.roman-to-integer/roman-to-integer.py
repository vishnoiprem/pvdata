class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I":1, "V": 5, "X":10,"L":50,"C":100, "D":500, "M":1000}
        ans = 0
        for i in range(0, len(s) - 1):
            c = s[i]
            cafter = s[i + 1]
            if d[c] < d[cafter]:
                ans -= d[c]
            else:
                ans += d[c]
        ans = ans+d[s[-1]]
        return ans


print(Solution().romanToInt("XXXIII"))



# Time:  O(n)
# Space: O(1)
#
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the xrange from 1 to 3999.
#
class Solution:
    # @return an integer
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        decimal = 0
        for i in range(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            else:
                decimal += numeral_map[s[i]]
        return decimal

if __name__ == "__main__":
    print (Solution().romanToInt("IIVX"))
    print (Solution().romanToInt("MMMCMXCIX"))