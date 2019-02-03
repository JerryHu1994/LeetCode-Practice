class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()
        for i in A:
            if i in s:
                return i
            s.add(i)