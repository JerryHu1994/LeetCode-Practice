class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parentmap = set()
        for i in range(n):
            if leftChild[i] != -1:
                if leftChild[i] in parentmap:   return False
                parentmap.add(leftChild[i])
        for i in range(n):
            if rightChild[i] != -1:
                if rightChild[i] in parentmap:  return False
                parentmap.add(rightChild[i])
        if n - len(parentmap) != 1: return False
        root = -1
        for i in range(n):
            if i not in parentmap:
                root = i
        print (root)
        q = [root]
        visited = set(q)
        while len(q):
            nextq = []
            for nextn in q:
                if leftChild[nextn] != -1:
                    nextq.append(leftChild[nextn])
                    if leftChild[nextn] not in visited:
                        visited.add(leftChild[nextn])
                    else:
                        return False
                if rightChild[nextn] != -1:
                    nextq.append(rightChild[nextn])
                    if rightChild[nextn] not in visited:
                        visited.add(rightChild[nextn])
                    else:
                        return False
            q = nextq
        return len(visited) == n
