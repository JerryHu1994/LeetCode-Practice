class Solution:
    
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 0, 0)]
        dep = left = ret = 0
        while len(queue):
            currnode, currdep, currpos = queue.pop(0)
            if currdep == dep:
                ret = max(currpos - left + 1, ret)
            else:
                dep = currdep
                left = currpos
            if currnode.left != None:
                queue.append((currnode.left, currdep+1, 2*currpos))
            if currnode.right != None:
                queue.append((currnode.right, currdep+1, 2*currpos+1))
        return ret