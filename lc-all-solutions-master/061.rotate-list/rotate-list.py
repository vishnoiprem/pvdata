# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        l = 1
        p = head
        while p.next:
            l += 1
            p = p.next
        k = k % l
        if k == 0:
            return head
        k = l - k % l - 1
        pp = head
        print (k)
        while k > 0:
            pp = pp.next
            k -= 1
        newHead = pp.next
        pp.next = None
        p.next = head
        return newHead
            
            
# Time:  O(n)
# Space: O(1)
#
# Given a list, rotate the list to the right by k places, where k is non-negative.
# 
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
        
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        n, cur = 1, head
        while cur.next:
            cur = cur.next
            n += 1
            print('cur',cur,n)
        cur.next = head

        cur, tail = head, cur
        #print(cur,tail)
        for _ in  range(n - k % n):
            print('__',_)
            tail = cur
            #print(cur)
            cur = cur.next
        tail.next = None

        return cur

    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print (Solution().rotateRight(head, 2))