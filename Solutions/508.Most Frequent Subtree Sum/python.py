# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, root):
        if root == None:
            return 0
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        s = left_sum+right_sum+root.val
        self.cnt[s] += 1
        return s
    
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        self.cnt = collections.Counter()   
        self.helper(root)
        max_ocur = self.cnt.most_common(1)[0][1]
        ret = []
        for num, count in self.cnt.items():
            if count == max_ocur:
                ret.append(num)
        return ret