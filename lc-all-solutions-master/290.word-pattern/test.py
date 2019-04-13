

def wordPattern(p,s):
	s=s.split()
	d={}
	if len(s)!=len(p):
		return False
	else:
		for i,c in enumerate(p):
			print(i,c)
			if c in d and not d[c]==s[i]:
				return False
			d[c]=s[i]
			print(d)
	return True

pattern = "abba"
str = "dog cat cat1 dog"
result=True
print(wordPattern(pattern,str))
