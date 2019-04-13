class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return [0]
        ans = [0] * (2 ** n) 
        ans[1] = 1
        mask = 0x01
        i = 1
        while i < n:
            mask <<= 1
            print(mask)
            for j in range(0, 2**i):
                root = (2**i)
                ans[root + j] = ans[root - j - 1] | mask
            i += 1
        return ans
            
#print(Solution().grayCode(2))


class Solution2(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        print('pp',1<<n)
        return [(i >> 1 )^ i for i in range(1 << n)]


if __name__ == "__main__":
    print (Solution2().grayCode(2))
