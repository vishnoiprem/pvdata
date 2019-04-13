# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        res, stack = [], [(1, root)]
        while stack:
            p = stack.pop()
            if not p[1]: continue
            stack.extend([(1, p[1].right), (1, p[1].left), (0, p[1])]) if p[0] != 0 else res.append(p[1].val)
        return res


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
	    self.val = x
	    self.left = None
	    self.right = None



class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        if root == None:
            return []
        else:
            preorderList = []
            stack = []
            stack.append(root)
            while(stack != []):
                node = stack.pop()
                preorderList.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return preorderList

a=TreeNode(1)
a.left=TreeNode(2)
a.right=TreeNode(3)
a.left.left=TreeNode(9)
a.left.right=TreeNode("Prem")
print(a.val)


print(Solution().preorderTraversal(a))