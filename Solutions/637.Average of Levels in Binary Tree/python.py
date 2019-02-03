# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue,ret = [], []
        queue.append([root, 0])
        currlevel, currlist = 0, []
        while len(queue):
            curr = queue.pop(0)
            if  curr[1]==currlevel:
                currlist.append(curr[0].val)
            else:
                ret.append(float(sum(currlist))/float(len(currlist)))
                currlist = [curr[0].val]
                currlevel+=1
            if curr[0].left:    queue.append([curr[0].left,curr[1]+1])
            if curr[0].right!=None: queue.append([curr[0].right,curr[1]+1])
        ret.append(float(sum(currlist))/float(len(currlist)))
        return ret
            
            
        