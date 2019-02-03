class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        currlen = 1
        while True:
            if reader.get(currlen-1) ==  target:
                return currlen-1
            elif reader.get(currlen-1) < target:
                currlen = currlen*2
            else:
                break
        left, right = currlen/2-1, currlen-1
        while left <= right:
            mid = int((left+right)/2)
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                left = mid+1
            else:
                right = mid-1
        return -1
            
        