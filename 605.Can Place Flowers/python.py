class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ind = 0
        count = 0
        while ind < len(flowerbed):
            if flowerbed[ind] == 0 and (ind == 0 or flowerbed[ind-1]==0) and (ind==len(flowerbed)-1 or flowerbed[ind+1]==0):
                flowerbed[ind] = 1
                count += 1
                ind += 2
            else:
                ind += 1
            print ind
        return count >= n