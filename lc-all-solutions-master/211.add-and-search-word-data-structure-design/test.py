class Tree(object):
    def __init__(self,x):
        self.left = None
        self.right = None
        self.data = x


root = Tree("root")
root.left = Tree("left")
root.right = Tree("right")
root.right.data = "right"