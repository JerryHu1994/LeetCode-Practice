# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:    return []
        currlist, nextlist, count, ret = [root], [], 0, [[root.val]]
        while len(currlist):
            while len(currlist):
                curr = currlist.pop(0)
                if curr.left != None:   nextlist.append(curr.left)
                if curr.right != None:   nextlist.append(curr.right)
            if len(nextlist):
                if count % 2==0:
                    ret.append([i.val for i in nextlist[::-1]])
                else:
                    ret.append([i.val for i in nextlist])
            currlist = nextlist
            nextlist = []
            count += 1 
        return ret        