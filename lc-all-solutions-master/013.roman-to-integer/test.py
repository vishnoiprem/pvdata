
class Solution(object):


	def romanToInt(self,s):



		roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

		result=0
		for i in range(0,len(s)-1):
			c=s[i]
			cafter=s[i+1]

			if roman[c] < roman[cafter]:
				result=result-roman[c]
			else:
				result=result+roman[c]
		result=result+roman[s[-1]]
		return result


if __name__ == "__main__":
    print (Solution().romanToInt("IXXII"))