class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)==0 and len(B)==0: return True
        for i in range(len(A)):
            if A[i:] + A[0:i] == B:
                return True
        return False
        