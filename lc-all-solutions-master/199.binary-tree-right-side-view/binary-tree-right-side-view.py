# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root, h):
            print(h,'root',ans)
            if root:
                if h == len(ans):
                    ans.append(root.val)
                dfs(root.right, h + 1)
                print('pp',h,ans)
                dfs(root.left, h + 1)
        ans = []
        dfs(root, 0)
        return ans


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    result = Solution().rightSideView(root)
    print (result)
