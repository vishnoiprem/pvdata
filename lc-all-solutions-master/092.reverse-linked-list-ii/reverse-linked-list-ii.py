# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        def reverse(root, prep, k):
            cur = root
            pre = None
            next = None
            while cur and k > 0:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
                k -= 1
            root.next = next
            prep.next = pre
            return pre
            
        dummy = ListNode(-1)
        dummy.next = head
        k = 1
        p = dummy
        start = None
        while p:
            if k == m:
                start = p
            if k == n + 1:
                reverse(start.next, start, n - m + 1)
                return dummy.next
            k += 1
            p = p.next



# Time:  O(n)
# Space: O(1)
#
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# 
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# 
# return 1->4->3->2->5->NULL.
# 
# Note:
# Given m, n satisfy the following condition:
# 1 <= m <= n <= length of list.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        diff, dummy, cur = n - m + 1, ListNode(-1), head
        dummy.next = head
        print(diff,dummy,head,cur)
        
        last_unswapped = dummy
        while cur and m > 1:
            cur, last_unswapped, m = cur.next, cur, m - 1
            print('fist loop ',cur, last_unswapped, m)
            
        prev, first_swapped = last_unswapped,  cur
        while cur and diff > 0:
            cur.next, prev, cur, diff = prev, cur, cur.next, diff - 1
            #print('second loop',cur, prev, cur, diff)
            print('second loop',diff,cur)
        #print('outside',last_unswapped)
        last_unswapped.next, first_swapped.next = prev, cur
        
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print (head)
    print (Solution().reverseBetween(head, 2, 4))