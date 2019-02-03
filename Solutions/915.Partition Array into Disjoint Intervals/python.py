class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        leftmax, maxlist = float("-inf"), []
        for n in A:
            leftmax = max(n, leftmax)
            maxlist.append(leftmax)
        rightmin, minlist = float("inf"), []
        for n in A[::-1]:
            rightmin = min(n, rightmin)
            minlist.append(rightmin)
        minlist = minlist[::-1]
        for i in range(len(A)-1):
            if maxlist[i] <= minlist[i+1]:  return i+1
        return len(A)