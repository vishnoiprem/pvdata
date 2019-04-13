class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def histogram(height):
            if not height:
                return 0
            height.append(-1)
            stack = []
            ans = 0
            for i in range(0, len(height)):
                while stack and height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1 if stack else i
                    ans = max(ans, h * w)
                stack.append(i)
            return ans
        ans = 0
        dp = [[0] * len(matrix[0]) for _ in range(0, len(matrix))]
        for i in reversed(range(0, len(matrix))):
            if i == len(matrix) - 1:
                dp[i] = [int(h) for h in matrix[i]]
            else:
                for j in range(0, len(matrix[0])):
                    if matrix[i][j] != "0":
                        dp[i][j] = dp[i + 1][j] + 1
            ans = max(ans, histogram(dp[i]))
        return ans
                

r = Solution()
print(r.maximalRectangle([
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0],
]))


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])

        T = [[0 for _ in range(row + 1)] for _ in range(col + 1)]
        maxArea = 0
        print(T)
        for i in range(row):
            for j in range(col):

                val = matrix[i][j]
                if val in ['1', 1]:
                    print (i,j,val)
                    T[i][j] = 1 if i == 0 else T[i-1][j] +1
        print (T)


r = Solution()
r.maximalRectangle([
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0],
])
