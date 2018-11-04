class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if 1 not in A:  return [0, len(A)-1]
        n = len(A)
        left, right = [-1]*n, [-1]*n
        index = A.index(1)
        for i in range(n):
            if i >= index:  left[i] = index
        index = n
        for i in range(n-1, -1, -1):
            right[i] = index
            if A[i] == 1:   index = i
        for i in range(n-2):
            # i represents end of the first number
            first_s = left[i]
            if first_s == -1:   continue
            l = i-first_s+1
            first_e = i
            second_s = right[i]
            second_e = second_s+l-1
            if second_e >= n:   break
            third_s = right[second_e]
            third_e = third_s+l-1
            # no answer
            if third_s >= n:    break
            if n - third_s != l:    continue # third len not right
            if A[first_s:first_e+1] == A[second_s:second_e+1] == A[third_s:third_e+1]:
                return [i, second_e+1]
        return [-1, -1]