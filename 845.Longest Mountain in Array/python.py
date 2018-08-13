class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        curr = 0
        currstart = 0
        while curr < len(A):
            up, down, equal = False, False, False
            while curr + 1 < len(A) and A[curr] < A[curr+1]:
                up = True
                curr += 1
            while curr + 1 < len(A) and A[curr] == A[curr+1]:
                curr += 1
                currstart = curr
                equal = True
                break
            if equal:   continue
            while curr + 1 < len(A) and A[curr] > A[curr+1]:
                print curr
                down = True
                curr += 1
            if up and down:
                ret = max(ret, curr - currstart + 1)
                currstart = curr
            else:
                currstart = curr
            if curr == len(A)-1:    break
        return ret
            