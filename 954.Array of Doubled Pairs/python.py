class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        pos, neg = [i for i in A    if i > 0], [-i for i in A   if i < 0]
        sortedpos, sortedneg = sorted(pos), sorted(neg)
        if len(sortedpos) % 2 or len(sortedneg)%2:  return False
        
        def helper(sort):
            while len(sort):
                currsmall = sort.pop(0)
                search = bisect.bisect_right(sort, currsmall*2)
                if sort[search-1] != currsmall*2:
                    print sort
                    return False
                else:
                    sort.pop(search-1)
            return True
        return helper(sortedpos) and helper(sortedneg)