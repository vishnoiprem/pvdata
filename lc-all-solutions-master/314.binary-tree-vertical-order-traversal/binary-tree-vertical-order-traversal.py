from collections import defaultdict
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(p, i, j, res):
            if p:
                res[j].append((p.val, i))
                self.leftMost = min(j, self.leftMost)
                dfs(p.left, i + 1, j - 1, res)
                dfs(p.right, i + 1, j + 1, res)
                
        self.leftMost = float("inf")
        ans = []
        res = defaultdict(list)
        dfs(root, 0, 0, res)
        i = self.leftMost
        while True:
            if not res[i]:
                break
            ans.append([item[0] for item in sorted(res[i], key=lambda a:a[1])])
            i += 1
        return ans


from collections import defaultdict
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution2(object):

    def __init__(self):


        self.minny = float("inf")
        self.maxxy = float("-inf")

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        """
        d = defaultdict(list)

        def sub(root, i):

            self.minny = min(self.minny, i)
            self.maxxy = min(self.minny, i)

            if not root:
                return


            d[i].append(root.val)


            sub(root.left, i - 1)
            sub(root.right,i +1)

        sub(root, 0)
        d = dict(d)
        print (d.keys())

        return [d[i] for i in range(self.minny + 1, self.maxxy + 1)]

root =TreeNode(10)
root.left=TreeNode(7)
root.right=TreeNode(11)
root.left.left=TreeNode(4)



print(Solution2().verticalOrder(root))


