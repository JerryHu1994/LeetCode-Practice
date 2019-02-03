# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:    return []
        queue, left, right, hashmap = [], 0, 0, {}
        queue.append([root,0])
        #add all the nodes into the hashmap
        while len(queue):
            curr = queue.pop(0)
            if not curr[1] in hashmap:
                hashmap[curr[1]] = [curr[0].val]
            else:
                hashmap[curr[1]].append(curr[0].val)
            if curr[0].left!=None:
                queue.append([curr[0].left, curr[1]-1])
                left = min(curr[1]-1, left)
            if curr[0].right!=None:
                queue.append([curr[0].right, curr[1]+1])
                right = max(curr[1]+1, right)
        #copy everything back to a list
        ret = []
        for i in range(left, right+1, 1):
            ret.append(hashmap[i])
        return ret
            
        