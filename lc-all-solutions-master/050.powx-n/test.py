class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n < 0 and n != -n:
            return 1.0 / self.myPow(x, -n)

        if n==0:
        	return 1
        print(n,'n')
        res=self.myPow(x,n//2)
        print(res,'res',n)
       	if n%2==0:
       		return res*res
       	else:
       		return x*res*res





if __name__ == "__main__":
    print (Solution().myPow(2, 4))