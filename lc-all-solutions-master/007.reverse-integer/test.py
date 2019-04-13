


def reverseDigit(s):
	sign="+"
	if s<0:
		sign="-"
		s=s*-1

	s1=""

	while s:

		carry=s%10
		if carry>0:
			s1=s1+str(carry)
		s=s//10



	if pow(2,31)>int(s1):
		print(sign+s1)
	else:
		print(0,pow(2,31))


print(reverseDigit(-1000000000000000000))





class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=x<0 and -1 or 1
        x = abs(x)
        ans = 0

        while x:
            ans = ans * 10 + x % 10
            x = x//10
        return sign * ans if ans <= 0x7fffffff else 0



print(Solution().reverse(123))



d={}


for i ,c in enumerate("abcdefghijklmnopqrstuvwxyz"):
	d[c]=i+1


print(d)


s="abccddde"
n=len(s)

cal=[]
prev=0
i=1




cal.append(d[s[0]])
while i<=n-1:
	if  d[s[i]] not  in cal:
		cal.append(d[s[i]])
	current=i
	if s[prev]==s[current]:
		temp=s[prev:current+1]
		cal.append(d[temp[0]]*len(temp))
	else:
		prev=i
	i=i+1






