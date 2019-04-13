

class twoSum(object):


	def __init__(self):

		self.num={}


	def add(self,number):

		self.num[number]=self.num.get(number,0)+1

	def find(self,value):
		d=self.num

		for num in d:
			t=value-num

			if t in  d:
				if t==num:
					if d[t]>=2:
						return True
					else:
						return False
		return False

# Your TwoSum object will be instantiated and called as such:

twoSum = twoSum()
number=1

twoSum.add(number) 
value=2
twoSum.find(value)