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

	def partition(self,head,k):


		pre=post=ListNode(-1)
		p=dumpy=ListNode(-1)
		p.next=head

		while p and p.next:

			if p.next.val<k:
				pre.next=p.next
				p.next=p.next.next
				pre=pre.next

			else:
				p=p.next
		pre.next=dumpy.next

		return post.next



if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    print (Solution().partition(head, 2))