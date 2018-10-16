class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right, l = 0, len(citations)-1, len(citations)
        while left <= right:
            mid = (left+right)/2
            midval = citations[mid]
            rightlen = l-mid
            if midval == rightlen:  return midval
            if midval > rightlen:
                right = mid - 1
            else:
                left = mid + 1
        return l-left