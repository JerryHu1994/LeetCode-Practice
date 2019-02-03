class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0 or len(A) == 1 or len(A) == 2:  return len(A)
        signs = []
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                signs.append(1)
            elif A[i] > A[i+1]:
                signs.append(-1)
            else:
                signs.append(0)
        curr = signs[0]
        currcnt = 1 if curr != 0 else 0
        ans = currcnt+1
        for s in signs[1:]:
            if curr == 1:
                if s == -1:
                    currcnt += 1
                else:
                    currcnt = 0 if s == 0 else 1
            elif curr == -1:
                if s == 1:
                    currcnt += 1
                else:
                    currcnt = 0 if s == 0 else 1
            else:
                currcnt = 0 if s == 0 else 1
            curr = s
            ans = max(ans, currcnt+1)
        return ans