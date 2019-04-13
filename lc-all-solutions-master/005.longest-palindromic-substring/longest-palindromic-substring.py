class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = right = 0
        n = len(s)
        for i in range(n - 1):
            if 2 * (n - i) + 1 < right - left + 1:
                break
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
        return s[left:right + 1]

    def longestPalindrome1(self, str1):
        n1=len(str1)
        print(n1)
        palindromeBeginsAt=0
        max_len=1
        palindrome= [[[False] for i in range(n1)] for i in range(n1)]
        print(palindrome)
        #singale character make as True
        for ii in range(n1):
            palindrome[ii][ii]=[True]


        for jj in range(n1-1):

            if str1[jj]==str1[jj+1]:
                palindrome[jj][jj+1] = [True]
                palindromeBeginsAt = jj
                print(palindromeBeginsAt)
                max_len = 2
        print(palindrome)



        #for _in in range(n1):
        #    print(palindrome[0][0])
        #print(palindrome)
        #print(palindrome)

        for curr_len in range(3,n1+1,1):
            for iii in range(0,n1-curr_len+1,1):
                jj=iii+curr_len-1
                print(str1[iii],str1[jj],palindrome[iii+1][jj-1][0])

                if (str1[iii]==str1[jj] and palindrome[iii+1][jj-1][0]):#1. The first and last characters should match 
                    print(str1[iii],str1[jj])
                    palindrome[iii][jj] = [True]
                    palindromeBeginsAt = iii
                    max_len = curr_len
                    print(palindromeBeginsAt,max_len,palindromeBeginsAt,palindrome[iii+1][jj-1][0])
        return str1[palindromeBeginsAt:(max_len + palindromeBeginsAt)]



s= Solution()
#print(s.abc('aaba'))
#print(s.abc('abaxabaxabaa'))
print(s.longestPalindrome1('abba'))

