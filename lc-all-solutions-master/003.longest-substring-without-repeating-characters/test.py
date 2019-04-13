
def longestSubString(s):
	NO_OF_CHAR=256
	l=len(s)
	cur_len=1
	max_len=1
	#i=0
	prev_index=0

	visited=[-1]*NO_OF_CHAR
	visited[ord(s[0])]=0

	for i,c in enumerate(visited):
		if c==0:
			print(i,c)

	for i in range(1,l):
		prev_index=visited[ord(s[i])]
		print(prev_index,i - cur_len > prev_index,i,cur_len, prev_index)
		if prev_index == -1 or (i - cur_len > prev_index):
			cur_len+=1
		else:
			if cur_len > max_len:
				max_len = cur_len
			cur_len = i - prev_index
			print(i,prev_index,cur_len,'cur')
		visited[ord(s[i])] = i

	if cur_len > max_len:
		max_len = cur_len
	return max_len


#print(longestSubString("abcabc"))
 

def longestSubString1(s):
	d={}
	start=0
	ans=0
	for i,c in enumerate(s):
		#print(i,c)
		if c in d:
			start=max(start, d[c]+1)
			print(start)
		ans=max(ans,i-start+1)
		d[c]=i
	return ans
	#print(d)

print(longestSubString("abccddddd"))

