class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret, sortedA = 0, sorted(A)
        for i in range(1, len(sortedA)):
            if sortedA[i] <= sortedA[i-1]:
                ret += sortedA[i-1] + 1 - sortedA[i]
                sortedA[i] = sortedA[i-1] + 1
        return ret