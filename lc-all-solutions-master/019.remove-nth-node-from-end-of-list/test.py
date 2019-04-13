# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
    	"""

    	dumppy=ListNode(1)
    	fast=slow=head
    	dumppy.next=head

    	while n and fast.next:
    		n-=1
    		fast=fast.next

    	while fast.next ans slow.next:
    		fast=fast.next
    		slow=slow.next
    	slow.next=slow.next.next
