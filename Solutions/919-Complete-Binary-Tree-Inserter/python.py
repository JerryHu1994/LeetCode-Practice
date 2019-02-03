# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        if self.root == None:   return
        self.queue, self.nextqueue = [root], []
        valid = True
        while valid:
            while len(self.queue):
                n = self.queue[0]
                if n.left == None:
                    valid = False
                    break
                else:
                    self.nextqueue.append(n.left)
                if n.right == None:
                    valid = False
                    break
                else:
                    self.queue.pop(0)
                    self.nextqueue.append(n.right)
            if valid:
                self.queue = self.nextqueue
                self.nextqueue = []
        
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        newnode = TreeNode(v)
        first = self.queue[0]
        if first.left == None:
            first.left = newnode
        elif first.right == None:
            first.right = newnode
            self.queue.pop(0)
        self.nextqueue.append(newnode)
        if len(self.queue) == 0:    self.queue, self.nextqueue = self.nextqueue, []
        return first.val
            
    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()