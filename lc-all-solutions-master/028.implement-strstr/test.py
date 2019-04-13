class Solution(object):


	def strStr(self, haystack, needle):

		if len(haystack)<1 and len(needle):
			return 1


		n=len(needle)
		for i in range(len(haystack)):
			#print(haystack[i:i+n],i)
			if haystack[i:i+n]==needle:
				return i

		return -1


    
if __name__ == "__main__":
    print (Solution().strStr("hello", "ll"))