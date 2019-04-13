class Solution(object):
    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
            
        ans = 1
        while n > 0:
            if n & 0x01:
                ans *= x
            x *= x
            n >>= 1
        return ans


    def myPow(self,x,n):
        n1=1
        if n<0:
            x=1 / x
            n=-n
        ans=1*x

        while n>0:

            ans=ans*n1
            print(x,ans,n1)

            n=n-1
            n1=n1+1
        print('prem',ans)
        return ans



#print(Solution().myPow(2,-2))

#print(4 & 0x01)

# Time:  O(logn)
# Space: O(logn)
# Recursive solution.
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0 and n != -n:
            print('n<0')
            return 1.0 / self.myPow(x, -n)
        if n == 0:
            print('n')
            return 1
        v = self.myPow(x, n // 2)
        print(v,'v')
        if n % 2 == 0:
            print(v)
            return v * v
        else:

            print(v)

            return v * v * x


if __name__ == "__main__":
    print (Solution().myPow(2, 4))
    #print (Solution().myPow(3, -5))