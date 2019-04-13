# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        else:
            stack = []
            out_stack = []
            stack.append(root)
            while stack != []:
                current = stack.pop()
                out_stack.append(current.val)
                if current.left != None:
                    stack.append(current.left)
                if current.right != None:
                    stack.append(current.right)
            return out_stack[::-1]


root=TreeNode(1)
root.right=TreeNode(2)
root.right.left=TreeNode(3)

print(Solution().postorderTraversal(root))

root=None

print(Solution().postorderTraversal(root))
