class ListNode(object):

	def __init__(self,data):
		self.val=data
		self.next=None

	def __repr__(self):

		if self is None:
			return 'Nil'
		else:
			return "{}-->{} ".format(self.val,repr(self.next))


class Solution(object):

	def deleteDuplicates(self,head):

		p=dummy=ListNode(None)
		p.next=head

		while p and p.next:

			if p.val==p.next.val:
				p.next=p.next.next

			else:
				p=p.next
		return dummy.next




if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    print (Solution().deleteDuplicates(head))