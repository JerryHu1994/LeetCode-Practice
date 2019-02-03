class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        A, mod, globalcnt, res = sorted(A), 10**9 + 7, collections.Counter(A), []
        for i in range(len(A)-2):
            if i > 0 and A[i] == A[i-1]:    continue
            left, right = i+1, len(A)-1
            while left < right:
                if A[left] + A[right] == target - A[i]:
                    res.append([A[i], A[left], A[right]])
                    left += 1
                    right -= 1
                    while left < right and A[left] == A[left-1]:    left += 1
                    while left < right and A[right] == A[right+1]:    right -= 1
                elif A[left] + A[right] < target - A[i]:
                    left += 1
                else:
                    right -= 1
        ret = 0
        for p in res:
            currcnt, temp = collections.Counter(p), 1
            for i in currcnt:
                cnt, up, down = currcnt[i], 1, 1
                for j in range(cnt):
                    up *= globalcnt[i]-j
                    down *= j+1
                temp *= up/down
            ret += temp%mod
        return ret