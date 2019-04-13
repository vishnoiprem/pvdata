class Solution:


	def setMatrix(sel,matrix):

        colZeroFlag = False
        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                colZeroFlag = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:



print(Solution().setMatrix([[1,2,3],[1,2,3],[1,2,3]]))