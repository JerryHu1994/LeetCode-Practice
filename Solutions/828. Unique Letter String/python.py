class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        dic, ret = collections.defaultdict(list), 0
        for ind, char in enumerate(S):  dic[char].append(ind)
        for key in dic:
            currlist = dic[key]
            for ind,val in enumerate(currlist):
                front = val+1 if ind == 0 else val-currlist[ind-1]
                back = len(S)-val if ind == len(currlist)-1 else currlist[ind+1]-val
                ret += front*back
        return ret