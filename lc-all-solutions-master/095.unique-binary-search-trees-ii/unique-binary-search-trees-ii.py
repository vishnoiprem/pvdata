class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def clone(root, offset):
            if root:
                newRoot = TreeNode(root.val + offset)
                left = clone(root.left, offset)
                right = clone(root.right, offset)
                newRoot.left = left
                newRoot.right = right
                return newRoot
                
        if not n:
            return []
        dp = [[]] * (n + 1)
        dp[0] = [None]
        for i in range(1, n + 1):
            dp[i] = []
            for j in range(1, i + 1):
                for left in dp[j - 1]:
                    for right in dp[i - j]:
                        root = TreeNode(j)
                        root.left = left
                        root.right = clone(right, j)
                        dp[i].append(root)
        return dp[-1]


# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(4^n / n^(3/2)) ~= Catalan numbers
#
# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
# 
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]
                
                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")
                
                queue = queue[1:]
                
            while serial[-1] == "#":
                serial.pop()
                
            return repr(serial)
                
        else:
            return None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        print(n)
        return self.generateTreesRecu(1, n)
    
    def generateTreesRecu(self, low, high):
        result = []
        if low > high:
            result.append(None)
        for i in range(low, high + 1):
            left = self.generateTreesRecu(low, i - 1)
            right = self.generateTreesRecu(i + 1, high)
            for j in left:
                for k in right:
                    cur = TreeNode(i)
                    cur.left = j
                    cur.right = k
                    result.append(cur)
        return result

if __name__ == "__main__":
    print (Solution().generateTrees(1))