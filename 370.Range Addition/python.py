class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        arr = [0]*(length+1)
        for pair in updates:
            arr[pair[0]] += pair[2]
            arr[pair[1]+1] -= pair[2]
        cul, ret = 0, []
        for i in arr[:-1]:
            cul += i
            ret.append(cul)
        return ret