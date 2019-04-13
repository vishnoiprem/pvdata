# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, isLeft):
            if not root:
                return None
            left = helper(root.left, True)
            right = helper(root.right, False)
            ret = 0
            if left is None and right is None and isLeft:
                return root.val
            if left:
                ret += left
            if right:
                ret += right
            return ret
        
        ret = helper(root, False)
        if ret:
            return ret
        return 0
            
            
            
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution1(object):

    #def __init__(self):

    #    self.acc = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.acc = 0

        def f(root, collect):

            if not root:
                return

            f(root.left, True)

            if collect:

                if not root.left or not root.right:
                    self.acc = self.acc+root.val
            f(root.right, False)
        print('a')
        f(root, False)

        return self.acc


r=TreeNode(1)

r.left=TreeNode(2)
r.left.left=TreeNode(4)
r.right=TreeNode(3)
r.right.right=TreeNode(5)
#r.left.left=TreeNode(2)

print(Solution().sumOfLeftLeaves(r))
