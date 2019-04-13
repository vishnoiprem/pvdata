



class Solution(object):
    def isPalindrome(self, x):



        if x<0:
            x=-1*x


        copy=x
        rev=0


        while copy>0:

            rev=rev*10+copy%10
            copy=copy//10

        if x==rev:
            return True
        else:

            return False


print(Solution().isPalindrome(123))
