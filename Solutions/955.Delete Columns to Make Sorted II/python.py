class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        l = len(A[0])
        ret = 0
        check = [False]*(len(A)-1)
        for i in range(l):
            chars = [w[i]   for w in A]
            temp = []
            for j in range(len(A)-1):
                if check[j]:    continue
                if chars[j] < chars[j+1]:
                    temp.append(j)
                elif chars[j] > chars[j+1]:
                    ret += 1
                    break
            else:
                for k in temp:
                    check[k] = True
            if all(check):  return ret
        return ret