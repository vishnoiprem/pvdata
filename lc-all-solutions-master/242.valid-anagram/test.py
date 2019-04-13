

def validAnagram(s,t):

	if len(s)!=len(t):
		return False


	if sorted(s)!=sorted(t):
		return False
	else:
		return True



s = "anagram"
t = "nagaram"
s = "rat"
t= "car"


print(True==validAnagram(s,t))
