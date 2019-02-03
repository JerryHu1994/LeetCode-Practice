class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        dic = collections.defaultdict(list)
        for ind,val in enumerate(S):
            dic[val].append(ind)
        cnt = 0
        for w in words:
            curridx, valid = -1, True
            for c in w:
                if len(dic[c]) != 0:
                    pos = bisect.bisect_right(dic[c], curridx)
                    if pos != len(dic[c]):
                        curridx = dic[c][pos]
                    else:
                        valid = False
                        break
                else:
                    valid = False
                    break
            if valid:   cnt += 1
        return cnt
                
                