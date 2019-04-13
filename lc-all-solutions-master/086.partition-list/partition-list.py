# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        sHead = sDummy = ListNode(-1)
        p = dummy
        while p and p.next:
            if p.next.val < x:
                sDummy.next = p.next
                p.next = p.next.next
                sDummy = sDummy.next
            else:
                p = p.next
            # if you change p.next then make sure you wouldn't change p in next run
        sDummy.next = dummy.next
        return sHead.next
        
# Time:  O(n)
# Space: O(1)
#
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the two partitions.
# 
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
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
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        
        dummySmaller, dummyGreater = ListNode(-1), ListNode(-1)

        smaller, greater = dummySmaller, dummyGreater
        print(dummySmaller,smaller,greater,dummyGreater)
        
        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
                print('smlaar',smaller)
            else:
                greater.next = head
                greater = greater.next

                print('greater',greater)

            head = head.next
            
        smaller.next = dummyGreater.next

        greater.next = None
        print('p',smaller,greater,dummySmaller)
        
        return dummySmaller.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    print (Solution().partition(head, 2))

      
        
        