class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        return [int(i)  for i in str(int("".join([str(s) for s in A]))+K)]