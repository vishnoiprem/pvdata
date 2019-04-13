
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8


class ListNode(object):

	def __init__(self,x):
		self.val=x
		self.next=None

	def __str__(self):

		return "{}->{}".format(self.val, self.next)


class Solution(object):



	def addLinkedList(self,n1,n2):
		carry=0
		p=dummpy=ListNode(-1)

		while n1 and n2:
			p.next=ListNode(n1.val+n2.val+carry)
			carry=p.next.val//10
			p.next.val=p.next.val%10
			p=p.next
			n1=n1.next
			n2=n2.next

		res=n1 or n2

		while res:
			p.next=ListNode(res.val+carry)
			carry=p.next.val//10
			p.next.val=p.next.val%10
			p=p.next
			res.next


		if carry:
			p.next=ListNode(carry)
		return dummpy.next

		 


if __name__=="__main__":



	a=ListNode(1)
	a.next=ListNode(5)
	a.next.next=ListNode(10)
	print(a)
	b=ListNode(2)
	b.next=ListNode(4)
	b.next.next=ListNode(11)
	#b.next.next.next=ListNode(18)
	print(b)	
	print(Solution().addLinkedList(a,b))







