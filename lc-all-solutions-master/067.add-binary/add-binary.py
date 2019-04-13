class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        diff = abs(len(a) - len(b))
        if len(a) > len(b):
            b = "0" * diff + b
        else:
            a = "0" * diff + a
            
        ret = ""
        carry = 0
        ai, bi = len(a) - 1, len(b) - 1
        al, bl = len(a), len(b)
        while ai >= 0 and bi >= 0:
            ac, bc = a[ai], b[bi]
            if ac == "1" and bc == "1":
                if carry == 1:
                    ret += "1"
                else:
                    ret += "0"
                carry = 1
            elif ac == "0" and bc == "0":
                if carry == 1:
                    ret += "1"
                else:
                    ret += "0"
                carry = 0
            else:
                if carry == 1:
                    ret += "0"
                else:
                    ret += "1"

            ai -= 1
            bi -= 1

        if carry == 1:
            ret += "1"
        return ret[::-1]


# Time:  O(n)
# Space: O(1)
#
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".
#


class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            print(i)
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b): 
                val += int(b[-(i + 1)])
            carry, val = val //2, val % 2
            result += str(val)
        if carry:
            result += str(carry)
        return result[::-1]

if __name__ == '__main__':
    result = Solution().addBinary('11', '1')
    #c = bin(int(1,2) + int(11,2))
    #print(c)
    print (result)
            