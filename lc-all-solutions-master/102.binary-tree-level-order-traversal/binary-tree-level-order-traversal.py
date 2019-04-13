# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = [[root.val]]
        queue = deque([root])
        #print(queue)
        while queue:
            print(queue)
            levelans = []
            for _ in range(0, len(queue)):
                root = queue.popleft()
                if root.left:
                    levelans.append(root.left.val)
                    queue.append(root.left)
                if root.right:
                    levelans.append(root.right.val)
                    queue.append(root.right)
            if levelans:
                ans.append(levelans)
        return ans
    
                    
                
              
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().levelOrder(root)
    print (result ) 
            
# Time:  O(n)
# Space: O(n)
#
# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
# Definition for a  binary tree node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root:
            return []
        
        queue = []
        result = []
        queue.append(root)
        #print(queue)
        
        while queue:
            size = len(queue)
            print('SIZE',size)
            level = []
            
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                print('level',level)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().levelOrder(root)
    print (result ) 


