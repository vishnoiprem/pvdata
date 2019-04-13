

class ListNode(object):

	def __init__(self,x):
		self.val=x
		self.next=None

	def __repr__(self):

		return "{}-> {} ".format(self.val,repr(self.next))


class Solution:

	def rotateRight(self,head,k):

		p=dumppy=ListNode(-1)
		cur=head

		n=1
		while cur.next:
			n=n+1
			cur=cur.next
		cur.next=head

		tail=cur
		cur=head

		for i in range(n-n%k):
			#tail=tail.next
			tail = cur
			cur=cur.next

		tail.next=None

		return cur








if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print (Solution().rotateRight(head, 2))