class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        s = (C-A)*(D-B) + (G-E)*(H-F)
        x1, y1, x2, y2 = max(A, E), max(B, F), min(C, G), min(D, H)
        return s if x2 < x1 or y1 > y2 else s - (x2-x1)*(y2-y1)
        
                