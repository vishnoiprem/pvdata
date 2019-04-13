# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while p.next:
            if p.next.next and p.next.val == p.next.next.val:
                z = p.next
                while z and z.next and z.val == z.next.val:
                    z = z.next
                p.next = z.next
            else:
                p = p.next
        return dummy.next


# Time:  O(n)
# Space: O(1)
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
#  leaving only distinct numbers from the original list.
# 
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.next.val == cur.val:
                val = cur.val;
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        return dummy.next
    
if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(2), ListNode(3)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(4)
    head.next.next.next.next.next, head.next.next.next.next.next.next = ListNode(4), ListNode(5)
    print(head)
    print (Solution().deleteDuplicates(head))
    
    
    
def RemoveDuplicates(head):
    if head:
        node = head
        while node.next:
            if node.data == node.next.data:
                node.next = node.next.next
            else:
                node = node.next
    return head