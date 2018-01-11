# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        curr = root
        while curr != None:
            self.stack.append(curr)
            curr = curr.left
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)!=0
        
        

    def next(self):
        """
        :rtype: int
        """
        ret = self.stack.pop()
        right = ret.right
        if right!=None:
            self.stack.append(right)
            while right.left != None:
                right = right.left
                self.stack.append(right)
        return ret.val
        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())