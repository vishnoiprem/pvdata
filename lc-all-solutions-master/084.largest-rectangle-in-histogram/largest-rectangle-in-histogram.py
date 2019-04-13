class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        height.append(-1)
        stack = []
        ans = 0
        print(height)
        for i in range(0, len(height)):
            while stack and height[i] < height[stack[-1]]:
                print('-1',stack,stack[-1])
                h = height[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                print(h,w,'hw')
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans



if __name__ == "__main__":
    print (Solution().largestRectangleArea([2, 1, 2]))
    print (Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
# Time:  O(n)
# Space: O(n)
#
# Given n non-negative integers representing the histogram's bar 
# height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
# 
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.
#

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        increasing, area, i = [], 0, 0
        while i <= len(height):
            if not increasing or (i < len(height) and height[i] > height[increasing[-1]]):
                increasing.append(i)
                i += 1
            else:
                last = increasing.pop()
                if not increasing:
                    area = max(area, height[last] * i)
                else:
                    area = max(area, height[last] * (i - increasing[-1] - 1 ))
        return area

if __name__ == "__main__":
    print (Solution().largestRectangleArea([2, 1, 4]))
    print (Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))