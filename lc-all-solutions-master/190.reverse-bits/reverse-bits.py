class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        mask = 1
        for _ in range(32):
            ans <<= 1
            if mask & n:
                ans |= 1
            n >>= 1
            print(n)
        return ans


print(Solution().reverseBits(45))


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans=ans<< 1
            print(i,ans)
            ans=ans| n & 1
           # print(ans)
            n =n>> 1
        return ans

print(Solution().reverseBits(45))


