class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        s = set()
        for a in A:
            even_chars = sorted([a[i] for i in range(0, len(a), 2)])
            odd_chars = sorted([a[i] for i in range(1, len(a), 2)])
            currstr = "".join(even_chars) + "".join(odd_chars)
            if currstr not in s:
                s.add(currstr)
        return len(s)