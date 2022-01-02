# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if root == None:    return ""
        dq = collections.deque()
        dq.append((root, ""))
        found_start, found_end = False, False
        start_path, end_path = "", ""
        while len(dq) > 0 and not(found_start and found_end):
            node, path = dq.popleft()
            if node.val == startValue:
                found_start = True
                start_path = path
            elif node.val == destValue:
                found_end = True
                end_path = path
            if node.left != None:
                dq.append((node.left, path+"L"))
            if node.right != None:
                dq.append((node.right, path+"R"))
        i = 0
        while len(start_path) > i and len(end_path) > i and start_path[i] == end_path[i]:
            i += 1
        return (len(start_path)-i)*'U'+end_path[i:]
