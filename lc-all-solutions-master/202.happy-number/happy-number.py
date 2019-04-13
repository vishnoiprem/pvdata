class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = {}
        sq_sum = 0
        while n != 1:
            sq_sum = 0
            sub_num = n
            while sub_num > 0:
                sq_sum += (sub_num % 10) * (sub_num % 10)
                sub_num /= 10
            if sq_sum in record:
                return False
            else:
                record[sq_sum] = 1
            n = sq_sum
        return True

#r = Solution()
#print(r.isHappy(19))

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def split_sum(n):

            return sum([int(x) ** 2 for x in list(str(n))])
        i = 0

        new_sum = split_sum(n)

        while i < 10:
            new_sum = split_sum(new_sum)
            i += 1

        #print(new_sum)
        return i == 1

r = Solution()
print(r.isHappy(19))


# Time:  O(k), where k is the steps to be happy number
# Space: O(k)
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the sum 
# of the squares of its digits, and repeat the process until 
# the number equals 1 (where it will stay), or it loops endlessly 
# in a cycle which does not include 1. Those numbers for which 
# this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        lookup = {}
        while n != 1 and n not in lookup:
            lookup[n] = True
            print(lookup)
            n = self.nextNumber(n)
        return n == 1
    
    def nextNumber(self, n):
        new = 0
        for char in str(n):
            new = new+int(char)**2
        return new

r = Solution()
print(r.isHappy(19))
