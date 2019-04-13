

class Solution(object):

	def reverseInt(self, n):
		sign=1
		if n<0:
			n=-1*n
			sign=-1

		ans=0
		while n>0:

			ans=ans*10+n%10
			print(ans)
			n=n//10

		return  ans*sign if sign<1  else ans


print(Solution().reverseInt(120))