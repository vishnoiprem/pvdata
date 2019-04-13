# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        fast = slow = dummy

        while n and fast:
            fast = fast.next
            n -= 1
        
        while fast.next and slow.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next

    def listPrint(self,lst):

        while lst!=None:
            print(lst.val)
            lst=lst.next

            

#Given linked list: 1->2->3->4->5, and n = 2.

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)

e=ListNode(5)

n=2
#After removing the second node from the end, the linked list becomes 1->2->3->5.


head=a
a.next=b
b.next=c
c.next=d

d.next=e


s=Solution()
print(s.listPrint(head))



print(s.removeNthFromEnd(head,2))

print(s.listPrint(head))





class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        foo = []
        while True:

            foo.append(str(self.val))
            the_next = self.next
            self.val = the_next
            if not the_next:
                break
            self.next = the_next.next

        return '\t'.join([x for x in foo if x is not None])


class Solution(object):

    def length(self,xs):
        if xs is None:
            return 0
        else:
            return 1 + self.length(xs.next)


    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        def sub(curr,index, n, head,prev):
            if index == n:

                next_n = curr.next if curr else None

                prev.next = next_n

                return head
            else:

                return sub(curr.next, index + 1, n, head, curr)
        if n == 0:
            return head.next
        elif head.next is None:
            return None
        else:
            return sub(head, 1, n, head, head)



a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(5)



a.next = b
b.next = c
c.next = d
d.next = e


r = Solution()
print ('a',a)

x = r.removeNthFromEnd(a,2)
print (x)




        