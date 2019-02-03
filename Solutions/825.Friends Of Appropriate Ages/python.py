class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages = sorted(ages)
        ages = [float(i) for i in ages]
        ret, dic = 0, {} 
        for i in range(len(ages)):
            temp = 0
            if ages[i] in dic:
                ret += dic[ages[i]]
                continue
            ind = bisect.bisect_right(ages, ages[i])-1
            # i is friend A, 0 to i-1 is friend B
            blist = ages[0:ind]
            nextval = 0.5 * ages[i] + 7
            nextind = bisect.bisect_right(blist, nextval)
            nextblist = blist[nextind:]
            for j in nextblist:
                if not (j > 100 and ages[i] < 100): temp += 1
            dic[ages[i]] = temp
            ret += temp
        return ret