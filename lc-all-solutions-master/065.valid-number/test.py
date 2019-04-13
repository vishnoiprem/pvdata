class Solution:

	def isNumber(self,val):
		try:


			
			if  float(val):
				return True

			else:
				return True


		except:
			return False


if __name__ == "__main__":
    print (Solution().isNumber(".0"))
    print (Solution().isNumber("abc"))
    print (Solution().isNumber("1 a"))
    print (Solution().isNumber("2e10"))
    print(float(".0"))