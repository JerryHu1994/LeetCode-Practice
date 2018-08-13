class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        currlen = 0
        # find the position of K
        for i in range(len(S)):
            if S[i].isdigit():
                currlen *= int(S[i])
            else:
                currlen += 1
                if currlen == K:    return S[i]
            if currlen >= K:
                break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                currlen /= int(c)
                K = K%currlen
            else:
                # either K decrements to currlen or K is divided to currlen
                if K == currlen or K == 0:  return c
                currlen -= 1
                