class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        slen, tlen = len(S), len(T)
        start = -1
        sindex, tindex = 0, 0
        ans = slen
        while (sindex < slen):
            if S[sindex] == T[tindex]:
                tindex += 1
                # found a match
                if tindex == tlen:
                    end = sindex
                    tindex -= 1
                    # move t pointer backwards until it exhausts
                    while tindex >= 0:
                        while S[sindex] != T[tindex]:
                            sindex -= 1
                        sindex -= 1
                        tindex -= 1
                    sindex += 1
                    tindex += 1
                    if end-sindex+1 < ans:
                        ans = end-sindex+1
                        start = sindex
            sindex += 1
        return ""   if start == -1 else S[start:start+ans]