

class Solution(object):

	def removeDuplicates(self,nums):
		count=0

		d={}

		if len(nums)==1:
			return 1

		for i,c in enumerate (nums):
			if c in d:
				d[c]+=1
			else:
				d[c]=1
		#return d
		count=0
		for key, value in d.items():
			if value>1:
				count=count+value
		return count


if __name__ == "__main__":
    print (Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
    print (Solution().removeDuplicates([1]))



class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        
        last, i, same = 0, 1, False

        while i < len(A):

            if A[last] != A[i] or not same:
                last += 1
                A[last] = A[i]

                if A[last] == A[i]:
                	same=True
                else:
                	same=False
            i = i+1
            
        return last + 1

if __name__ == "__main__":
    print (Solution().removeDuplicates([1,]))
