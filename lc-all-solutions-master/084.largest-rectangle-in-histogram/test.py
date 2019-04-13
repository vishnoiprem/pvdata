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
        for i in range(0, len(height)):
            while stack and height[i] < height[stack[-1]]:
                print(i,'i','stack',stack)
                h = height[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                ans = max(ans, h * w)
                print(ans,'asn')
            stack.append(i)
        height.pop()
        return ans



if __name__ == "__main__":
    print (Solution().largestRectangleArea([]))    
    print (Solution().largestRectangleArea([2,1, 2, 3,1]))
    #print (Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))