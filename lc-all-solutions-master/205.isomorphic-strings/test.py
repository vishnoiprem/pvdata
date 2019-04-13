

def isIsomorphic(s,t):

	if len(s)!=len(t):
		return False


	if len(set(s))!=len(set(t))!=len(set(zip(s, t))):
		return False
	return True
s= "paper"
t= "title"

print(isIsomorphic(s,t))