class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        i,j = None, None
        for y in range(m):
            for x in range(n):
                # find one island
                if A[y][x] == 1:
                    i, j = y, x
                    break
            if i != None:   break
        queue, groups = [(i,j)], set([(i, j)])
        while len(queue):
            i, j = queue.pop(0)
            # up
            if i > 0 and A[i-1][j] == 1 and (i-1,j) not in groups:
                queue.append((i-1, j))
                groups.add((i-1, j))
            # down
            if i < m-1 and A[i+1][j] == 1 and (i+1, j) not in groups:
                queue.append((i+1, j))
                groups.add((i+1, j))
            # left
            if j > 0 and A[i][j-1] == 1 and (i, j-1) not in groups:
                queue.append((i, j-1))
                groups.add((i, j-1))
            # right
            if j < n-1 and A[i][j+1] == 1 and (i, j+1) not in groups:
                queue.append((i, j+1))
                groups.add((i, j+1))
        for p in groups:    A[p[0]][p[1]] = 2
        queue, cnt = list(groups), 0
        visited = set(queue)
        while True:
            nextq = []
            for node in queue:
                i, j = node
                # up
                if i > 0:
                    if A[i-1][j] == 1:  return cnt
                    if A[i-1][j] == 0 and (i-1,j) not in visited:
                        nextq.append((i-1, j))
                        visited.add((i-1, j))
                # down
                if i < m-1:
                    if A[i+1][j] == 1:  return cnt
                    if A[i+1][j] == 0 and (i+1, j) not in visited:
                        nextq.append((i+1, j))
                        visited.add((i+1, j))
                # left
                if j > 0:
                    if A[i][j-1] == 1:  return cnt
                    if A[i][j-1] == 0 and (i, j-1) not in visited:
                        nextq.append((i, j-1))
                        visited.add((i, j-1))
                # right
                if j < n-1:
                    if A[i][j+1] == 1:  return cnt 
                    if A[i][j+1] == 0 and (i, j+1) not in visited:
                        nextq.append((i, j+1))
                        visited.add((i, j+1))
            cnt += 1
            queue = nextq
