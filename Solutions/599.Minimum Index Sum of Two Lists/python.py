class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        maxlist = list1 if len(list1)>=len(list2) else list2
        minlist = list1 if len(list1)<len(list2) else list2
        bestrank = float("inf")
        ret = []
        for ind,val in enumerate(minlist):
            if val in maxlist:
                s = ind + maxlist.index(val)
                if s < bestrank:
                    bestrank = s
                    ret = [val]
                elif s==bestrank:
                    ret.append(val)
        return ret