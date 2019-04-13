
def containsDuplicate(numarr):


	dict={}


	for i,d in enumerate(numarr):
		print(i,d)

		if d in dict:
			return True
	return False


def containsDuplicate(numarr):
	numarr.sort()
	print(numarr)

	for i in range(len(numarr)-1):

		if numarr[i]==numarr[i+1]:
			print("duplicate")



print(containsDuplicate([1,2,3,4,1 ]))