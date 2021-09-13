# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def search(self, root: TreeNode, distance:int) -> (int, dict):
        if root == None:
            return (0, {})
        if root.left == None and root.right == None:
            d = {}
            d[1] = 1
            return (0, {0:1})
        (left_totalpairs, left_totaldic) =  self.search(root.left, distance)
        (right_totalpairs, right_totaldic) =  self.search(root.right, distance)
        total_count, total_dic = left_totalpairs + right_totalpairs, {}
        for lkey, lvalue in left_totaldic.items():
            for rkey, rvalue in right_totaldic.items():
                if lkey + rkey + 2 <= distance: total_count += lvalue*rvalue
        for lkey, lvalue in left_totaldic.items():
            total_dic[lkey+1] = lvalue
        for rkey, rvalue in right_totaldic.items():
            if rkey+1 in total_dic:
                total_dic[rkey+1] += rvalue
            else:
                total_dic[rkey+1] = rvalue
        return (total_count, total_dic)
    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if root == None:    return 0
        (totalpairs, totaldic) =  self.search(root, distance)
        return totalpairs