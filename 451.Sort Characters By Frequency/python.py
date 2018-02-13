class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        li = dic.items()
        li = sorted(li, key = lambda x: -x[1])
        ret = ""
        for i in li:
            ret += i[0]*i[1]
        return ret