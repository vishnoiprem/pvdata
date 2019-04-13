class TreeNode(object):

	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

class Solution(object):
	def isSmmetric(self,node):
		def helper(root,mirror):
			if not root and not mirror:
				return True
			if root and mirror and root.val==mirror.val:
				return helper(root.left,mirror.right) and helper(root.right,mirror.left)
		return helper(node, node)



if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)

    #root.left.right = TreeNode(4)
    #,root.left.left = TreeNode(2)
    root.right=TreeNode(2)

    result = Solution().isSmmetric(root)
    print (result)
