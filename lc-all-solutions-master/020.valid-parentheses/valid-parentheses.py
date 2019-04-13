class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = ["()", "[]", "{}"]
        for i in range(0, len(s)):
            stack.append(s[i])
            print(stack)
            if len(stack) >= 2 and stack[-2]+stack[-1] in d:
                print('stack[-2]',stack[-1])
                stack.pop()
                stack.pop()
        return len(stack) == 0
        

s=Solution()

print(s.isValid('[{}]'))





from collections import deque

class Solution1(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2:
            return False


        s = s.strip()
        stack = list()
        chars = ["(", "{", "["]
        other_half = [")", "}", "]"]
        #the_dict =["(")","{""}","[""]""]
        the_dict =list(zip(chars,other_half))
        print('the_dict',the_dict)

        for char in s:

            if char in chars:
                stack.append(char)
            elif char in other_half:
                if len(stack) == 0:
                    return False
                popped_off = stack.pop()
                
                expecting = (popped_off,char)
                #print(expecting)

                if expecting not in the_dict:
                    return False

        if len(stack):
            return False

        return True

r = Solution1()
print (r.isValid("([])]"))



