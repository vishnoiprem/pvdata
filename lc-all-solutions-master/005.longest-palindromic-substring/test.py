

Input="babad"
Output="bab"

#Note: "aba" is also a valid answer.

#Example1:

Input=" ab | 9999/ a "
Output=True


def longestPalindrom(s):

	l=0
	r=len(s)-1
	status=True
	while l<r:

		if not s[l] in "abcdefghijklmnopqrstuvw":
			l= l+1
		if  not s[r] in "abcdefghijklmnopqrstuvw":
			r=r-1

		if s[l]!=s[r] and s[l] in "abcdefghijklmnopqrstuvw" and  s[r] in "abcdefghijklmnopqrstuvw":
			return False
		else:
			l=l+1
			r=r-1
	return status

print(longestPalindrom(Input)==Output)



class Solution(object):

   def abc(self, str1):
        n1=len(str1)
        print(n1)
        palindromeBeginsAt=0
        max_len=1
        palindrome= [[[False] for i in range(n1)] for i in range(n1)]
        print(palindrome)
        #singale character make as True
        for ii in range(n1):
            palindrome[ii][ii]=[True]
        print(palindrome)


        for jj in range(n1-1):

            if str1[jj]==str1[jj+1]:
                palindrome[jj][jj+1] = [True]
                palindromeBeginsAt = jj

                max_len = 2


                max_len = 2

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




print(Solution().abc("aba"))
