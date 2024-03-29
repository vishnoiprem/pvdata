class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        if k > 0:
            stack = stack[:-k]
            #print(stack)
        #print (stack)
        return "".join(stack).lstrip("0") or "0"

a="1432219"
k = 3
print(Solution().removeKdigits(a,k))