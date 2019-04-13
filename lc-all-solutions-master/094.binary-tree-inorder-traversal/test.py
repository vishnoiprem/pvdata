
class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None


class Solution(object):

	def inOrderTraversal(self,root):
		if root==None:
			return []
		else:
			result=[]
			stack=[]
			node=root

			while stack or node:
				print(node,stack)
				if node:
					stack.append(node)
					node=node.left
				else:
					node=stack.pop()
					result.append(node.val)
					node=node.right
			return result


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(2)
    root.right=TreeNode(11)

    result = Solution().inOrderTraversal(root)
    print (result)

