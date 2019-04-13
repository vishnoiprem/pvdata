class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n, dp):
            for i in range(2, n):
                if dp[i] == 1:
                    k = i * i
                    if k >= n:
                        return
                    while k < n:
                        dp[k] = 0
                        k += i
        if n < 2:
            return 0
        ans = 0
        dp = [1] * n
        dp[0] = 0
        dp[1] = 0
        helper(n, dp)
        # for i in xrange(0, n):
        #     if dp[i] == 1:
        #         print i + 1
                
        return sum(dp)
            

    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        #print(primes)
        primes[0] = primes[1] = False
        print(primes)
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)


print(Solution().countPrimes(10))
print(Solution().countPrimes2(10))