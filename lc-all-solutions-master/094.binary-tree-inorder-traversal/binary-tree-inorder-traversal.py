# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution11(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], [(1, root)]
        while stack:
            p = stack.pop()
            if not p[1]: continue
            stack.extend([(1, p[1].right), (0, p[1]), (1, p[1].left)]) if p[0] != 0 else res.append(p[1].val)
        return res


# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, curr = [], root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right
            
                if node.right is None:
                    node.right = curr
                    curr = curr.left
                else:
                    result.append(curr.val)
                    node.right = None
                    curr = curr.right
                
        return result


# Time:  O(n)
# Space: O(h)
# Stack Solution
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        print('stack',stack)
        i=0
        while stack:
            root, is_visited = stack.pop()
            print(i,root,is_visited,stack)
            i=i+1
            if root is None:
                print('continue')
                continue
            if is_visited:
                result.append(root.val)
                print(result)
            else:
                stack.append((root.right, False))
                stack.append((root, True))
                stack.append((root.left, False))

                print(9,stack)
        return result


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(2)

    result = Solution2().inorderTraversal(root)
    print (result)


    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    #result = Solution2().inorderTraversal(root)


# Definition for a binary tree node.
# class TreeNode:
# # # #
def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if root == None:
            return []
        else:
            result = []
            stack = []
            node = root
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    result.append(node.val)
                    node = node.right
            return result
    #print (result)