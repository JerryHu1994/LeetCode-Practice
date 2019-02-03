class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even, odd = [], []
        for i in A:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)
        return even + odd