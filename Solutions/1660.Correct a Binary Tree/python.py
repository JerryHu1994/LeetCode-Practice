# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        parent = {}
        visited = set()
        queue = []
        queue.append(root)
        visited.add(root.val)
        while len(queue) != 0:
            currnode = queue.pop(0)
            left, right = currnode.left, currnode.right
            if left != None:
                visited.add(left.val)
                queue.append(left)
                parent[left.val] = currnode
            if right != None:
                if right.val in visited:#found bad right child
                    parentnode = parent[currnode.val]
                    # try to find left or right
                    if parentnode.left != None and parentnode.left.val == currnode.val:
                        parentnode.left = None
                        break
                    if parentnode.right != None and parentnode.right.val == currnode.val:
                        parentnode.right = None
                        break
                visited.add(right.val)
                queue.append(right)
                parent[right.val] = currnode
        return root