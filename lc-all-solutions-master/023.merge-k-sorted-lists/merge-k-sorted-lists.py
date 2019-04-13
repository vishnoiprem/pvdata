# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        p = dummy = ListNode(-1)
        for i in range(0, len(lists)):
            node = lists[i]
            if not node:
                print('continue')
                continue
            heapq.heappush(heap, (node.val, node))
        print(heap)
        
        while heap:
            value, node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, node))
        print(heap)
        return dummy.next
            
 
    def listPrint(self,lst):

        while lst!=None:
            print(lst.val)
            lst=lst.next
       
        






a=ListNode(1)
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


l1=ListNode(1)
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
print(s.listPrint(head1))

print('first List')
print(s.listPrint(head2))
print('second list')

lst=[a,b]
print(len(lst))
print(lst)
ll=s.mergeKLists(lst)

print(ll.listPrint(ll))










