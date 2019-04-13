

class Solution(object):

	def isValid(self,s):

		open=["(","{","[" ]
		close=[")",'}',']']


		open_close=list(zip(open,close))

		stack=[]

		for c in s:

			if c in open:
				stack.append(c)
			elif c in close:
				if len(stack)==0:
					return False

				pop=stack.pop()

				comp_brak=(pop,c)

				if not comp_brak in open_close:

					return False




		if len(stack)>0:
			return False
		else:
			return True


print(Solution().isValid("[()]["))

