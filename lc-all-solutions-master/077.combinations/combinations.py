class Solution(object):
    def combine(self, n, k):
        print(n,k)
        if k==1:
            return [[i] for i in range(1,n+1)]
        elif k==n:
            return [[i for i in range(1,n+1)]]
        else:
            rs = []
            rs += self.combine(n-1,k)
            print('rs',rs)
            part = self.combine(n-1,k-1)
            
            print('part',part,rs)
            for ls in part:
                ls.append(n)
            rs += part
            return rs


if __name__ == "__main__":
    result = Solution().combine(4, 2)
    print (result)