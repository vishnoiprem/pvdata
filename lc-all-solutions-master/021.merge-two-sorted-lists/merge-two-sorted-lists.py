# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
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

ll=s.mergeTwoLists(head1, head2)

print(s.listPrint(ll))


#print(s.listPrint(head2))



        