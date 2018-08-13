class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = collections.Counter(S)
        maxfre = counter.most_common(1)[0][1]
        if maxfre > len(S) - maxfre + 1:
            return ""
        ret = [0 for i in range(len(S))]
        sortedkeys = [i[0] for i in counter.most_common()]
        count = 0 
        keyidx = 0
        retidx = 0
        while count != len(S):
            while counter[sortedkeys[keyidx]] > 0:
                counter[sortedkeys[keyidx]] -= 1
                ret[retidx] = sortedkeys[keyidx]
                retidx += 2
                count += 1
                if retidx >= len(S):    retidx = 1
            keyidx += 1
        return "".join(ret)
        
                