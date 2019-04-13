class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        sum = a ^ b
        print(sum)
        carry = (a & b) << 1
        print(carry,sum)
        return self.getSum(sum, carry)


print(Solution().getSum(8,9))