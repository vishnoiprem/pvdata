#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        
        """
        if p and q:
        	print(p.val,q.val)
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        


a1=TreeNode(10)
b1=TreeNode(8)
c1=TreeNode(12)
d1=TreeNode(6)
e1=TreeNode(14)

a1.left=b1
a1.right=c1

b1.left=d1
c1.right=e1


a2=TreeNode(10)
b2=TreeNode(8)
c2=TreeNode(12)
d2=TreeNode(6)
e2=TreeNode(14)


a2.left=b2
a2.right=c2

b2.left=d2
c2.right=e2


print(Solution().isSameTree(a1, a2))



from queue import Queue

class TreeNode():

    def __init__(self, x):
        self.root = x
        self.left = None
        self.right = None

class Solution():

    def isSameTree(self, p, q):

        queueOne = Queue()
        queueTwo = Queue()

        queueOne.put(p)
        queueTwo.put(q)

        while not queueOne.empty() and not queueTwo.empty():

            valOne = queueOne.get()
            valTwo = queueTwo.get()

            if valOne.root != valTwo.root():
                return False

            leftOne, rightOne = valOne.left, valOne.right
            leftTwo, rightTwo = valTwo.left, valTwo.right

            if leftOne:
                queueOne.put(leftOne)
            if rightOne:
                queueOne.put(rightOne)

            if leftTwo:
                queueTwo.put(leftTwo)
            if rightTwo:
                queueTwo.put(rightTwo)

        return queueOne.empty() and queueTwo.empty()

a1=TreeNode(10)
b1=TreeNode(8)
c1=TreeNode(12)
d1=TreeNode(6)
e1=TreeNode(14)

a1.left=b1
a1.right=c1

b1.left=d1
c1.right=e1


a2=TreeNode(10)
b2=TreeNode(8)
c2=TreeNode(12)
d2=TreeNode(6)
e2=TreeNode(14)


a2.left=b2
a2.right=c2

b2.left=d2
c2.right=e2


print(Solution().isSameTree(a1, a2))
