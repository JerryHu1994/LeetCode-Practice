# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:   return []
        queue, ret = [(root, 0)], []
        while len(queue):
            curr = queue.pop(0) 
            currnode, currlevel = curr[0], curr[1]
            if currnode.left!=None: queue.append((currnode.left, currlevel+1))
            if currnode.right!=None: queue.append((currnode.right, currlevel+1))
            if len(ret)==currlevel:
                ret.append([currnode.val])
            else:
                ret[currlevel].append(currnode.val)
        return ret
        