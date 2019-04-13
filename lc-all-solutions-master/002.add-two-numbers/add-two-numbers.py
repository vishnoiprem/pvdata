# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    # maybe standard version
    def _addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(-1)
        #print(p,dummy)
        carry = 0
        while l1 and l2:
            p.next = ListNode(l1.val + l2.val + carry)
            print('pval',p.val)
            carry = p.next.val // 10
            p.next.val =p.next.val%10
            p = p.next
            l1 = l1.next
            l2 = l2.next
        
        res = l1 or l2
        print('res',res)
        while res:
            p.next = ListNode(res.val + carry)
            carry = p.next.val / 10
            p.next.val %= 10
            p = p.next
            res = res.next
        if carry:
            p.next = ListNode(1)
        return dummy.next
    
    # shorter version
    def addTwoNumbers(self, l1, l2):
        p = dummy = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
            #print(l1,l1.val,l2,l2.val,carry)
            carry = val //10
            p.next = ListNode(val % 10)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            p = p.next
        return dummy.next
            


    def listPrint(self,lst):

        while lst!=None:
            print(lst.val)
            lst=lst.next


s=Solution()

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
z=ListNode(2)

a.next=b
b.next=c
c.next=d
d.next=z

e=ListNode(1)
f=ListNode(7)
g=ListNode(5)
h=ListNode(8)

e.next=f
f.next=g
g.next=h

print("Print List l1",s.listPrint(a))
print("Print List l2" ,s.listPrint(e))



ll=s._addTwoNumbers(a,e)
s.listPrint(ll)

print('second Method')
ll=s.addTwoNumbers(a,e)
s.listPrint(ll)
        