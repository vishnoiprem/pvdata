

def validParenthesis(p):

	if len(p)%2==1:
		return False


	open=['[','{','(']
	close=[']','}',')']

	open_close=list(zip(open,close))

	print(list(open_close))
	stack=[]

	for i,b in enumerate(p):

		if b in open:
			stack.append(b)
			print(b)
		elif b in close:
			if len(stack)<1:
				return False
	

			pop=stack.pop()
			expecting=(pop,b)
			#print(pop+b )

			if not expecting in open_close:
				return False

	if len(stack):
		return False

	return True




s="()[]{}"

print(validParenthesis(s))


	