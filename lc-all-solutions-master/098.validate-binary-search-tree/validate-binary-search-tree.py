# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev = -float("inf")
        stack = [(1, root)]
        while stack:
            p = stack.pop()
            if not p[1]:
                continue
            if p[0] == 0:
                if p[1].val <= prev:
                    return False
                prev = p[1].val
            else:
                stack.append((1, p[1].right))
                stack.append((0, p[1]))
                stack.append((1, p[1].left))
        return True
                
            
        
# Time:  O(n)
# Space: O(1)
# 
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Morris Traversal Solution
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def isValidBST(self, root):
        prev, cur = None, root
        while cur:
            if cur.left is None:
                if prev and prev.val >= cur.val:
                    return False
                prev = cur
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right
            
                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    if prev and prev.val >= cur.val:
                        return False
                    node.right = None
                    prev = cur
                    cur = cur.right
                
        return True


# Time:  O(n)
# Space: O(h)
class Solution2:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))
    
    def isValidBSTRecu(self, root, low, high):
        if root is None:
            return True
        
        return low <=root.val and root.val <=high \
            and self.isValidBSTRecu(root.left, low, root.val) \
            and self.isValidBSTRecu(root.right, root.val, high)

        
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(9)
    root.right = TreeNode(19)

    root.left.left = TreeNode(-5)
    root.right.right = TreeNode(21)
    root.right.left = TreeNode(17)


    print (Solution2().isValidBST(root))