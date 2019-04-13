
class Solution(object):

	def isPalindrome(self,s):

		l=0
		r=len(s)-1



		while l<=r:

			if not s[l].isalpha():
				l=l+1
				continue 

			if not s[r].isalpha():
				r=r-1
				continue

			if s[l].upper()!=s[r].upper():
				return False
			else:

				l=l+1
				r=r-1
		return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama" ))
print(Solution().isPalindrome("race a car"))



