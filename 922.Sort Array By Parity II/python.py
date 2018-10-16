class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = 1
        for i in range(0, len(A), 2):
            if A[i]%2:
                while odd < len(A):
                    if not A[odd]%2:
                        A[i], A[odd] = A[odd], A[i]
                        break
                    odd += 2
        return A