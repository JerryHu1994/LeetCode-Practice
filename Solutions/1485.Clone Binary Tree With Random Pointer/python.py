# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return None
        
        def dfs_copy(node):
            if not node:    return
            copy_dic[node] = NodeCopy(node.val)
            dfs_copy(node.left)
            dfs_copy(node.right)
        def dfs_connect(node):
            if not node:    return
            if node.left:
                copy_dic[node].left = copy_dic[node.left]
            if node.right:
                copy_dic[node].right = copy_dic[node.right]
            if node.random:
                copy_dic[node].random = copy_dic[node.random]
            dfs_connect(node.left)
            dfs_connect(node.right)
            return node
        copy_dic = {}
        dfs_copy(root)
        dfs_connect(root)
        return copy_dic[root]
        