
class ListNode(object):

	def __init__(self, x):
		self.data=x
		self.next=None

	def __str__(self):

		return "{} -> {}".format(self.data,self.next)


import heapq

class Solution:


	def mergeKSort(self,lists):

		heap=[]
		current=dummy=ListNode(-1)
		for node in lists:
			if node:
				heapq.heappush(heap, (node.data, node))
		print(heap)
		while heap:

			val,node=heapq.heappop(heap)
			current.next=node
			current=current.next

			if node.next:
				node = node.next
				heapq.heappush(heap, (node.data, node))

		return dummy.next


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
	print(Solution().mergeKSort([a,b]))