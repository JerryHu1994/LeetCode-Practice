class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        pts_a, pts_b, height, width = [], [], len(A), len(A[0])
        dis = collections.defaultdict(int)
        for j in range(height):
            for i in range(width):
                if A[j][i] == 1:    pts_a.append((j, i))
        for j in range(height):
            for i in range(width):
                if B[j][i] == 1:    pts_b.append((j, i))
        for pa in pts_a:
            for pb in pts_b:
                currdis = (pb[0]-pa[0], pb[1]-pa[1])
                dis[currdis] += 1
        if len(dis.values()) == 0:  return 0
        return max(dis.values())