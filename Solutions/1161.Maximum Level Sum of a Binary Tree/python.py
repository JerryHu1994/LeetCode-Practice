# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(int)
        def search(rootnode, level):
            if rootnode != None:
                dic[level] += rootnode.val
                if rootnode.left != None:
                    search(rootnode.left, level+1)
                if rootnode.right != None:
                    search(rootnode.right, level+1)
        search(root, 1)
        ans, maxval = 0, -sys.maxsize
        for key,val in dic.items():
            if val > maxval:
                ans = key
                maxval = val
        return ans
            