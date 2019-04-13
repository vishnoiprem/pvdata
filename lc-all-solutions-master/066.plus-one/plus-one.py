# Time:  O(n)
# Space: O(1)
#
# Given a non-negative number represented as an array of digits, plus one to the number.
# 
# The digits are stored such that the most significant digit is at the head of the list.



class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(range(0, len(digits))):
            print(i)
            digit = (digits[i] + carry) % 10
            carry = 1 if digit < digits[i] else 0
            digits[i] = digit
            print(digits)
        if carry == 1:
            return [1] + digits
        return digits


if __name__ == "__main__":
    print (Solution().plusOne([9, 9, 9, 9]))