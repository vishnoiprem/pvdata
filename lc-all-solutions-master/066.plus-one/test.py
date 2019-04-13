
class Solution:

	def plusOne(self,digits):



		carry=1
		for i in reversed(range(0,len(digits))):
			digit =(digits[i]+carry)%10

			carry=1 if digit<digits[i] else 0

			digits[i]=digit

		if carry:
			digits.insert(0,1)
		return digits

if __name__ == "__main__":
    print (Solution().plusOne([9, 9, 9, 9]))