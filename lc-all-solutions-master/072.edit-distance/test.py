




class Solution:

	def minDistance(self,word1,word2):

		T=[ [0]*(len(word2)+1)for _ in range (len(word1)+1) ]
		print(T)
		if len(word1)==0 or len(word2)==0:
			return max(len(word1),len(word2))

		for i in range(len(word1)+1):
			T[i][0]=i
		for i in range(len(word2)+1):
			T[0][i-1]=i

		for i in range(1,len(word1)+1):
			for j in range(1,len(word2)+1):

				if word1[i-1]==word2[j-1] :
					T[i][j]=T[i-1][j-1]

				else:
					T[i][j]=1+min(T[i-1][j],T[i-1][j-1],T[i][j-1])

		return T[-1][-1]


print(Solution().minDistance('a','b'))
                    