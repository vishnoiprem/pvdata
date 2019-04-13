class ListNode(object):

	def __init__(self,data):
		self.val=data
		self.next=None

import heapq


class Solution:

	def mergeKLists(self, lists):

		heap=[]
		p=dummy=ListNode(-1)

		for i in range(len(lists)):

			node=lists[i]

			heapq.heappush(heap,(node.val,node))

			
			print(i,heap)

		while heap:

			value,node=heapq.heappop(heap)
			p.next=node
			p=p.next

			if node.next:
				node=node.next
				heapq.heappush(heap, (node.val,node))

		return dummy.next








       
        


a=ListNode(10)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(5)

#After removing the second node from the end, the linked list becomes 1->2->3->5.


head1=a
a.next=b
b.next=c
c.next=d
d.next=e


l1=ListNode(9)
l2=ListNode(2)
l3=ListNode(3)
l4=ListNode(4)
l5=ListNode(5)

n=2
#After removing the second node from the end, the linked list becomes 1->2->3->5.


head2=l1
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5





s=Solution()

print('first List')
print('second list')

lst=[a,l1]
ll=s.mergeKLists(lst)



