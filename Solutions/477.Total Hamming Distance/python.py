class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret,n = 0, len(nums)
        for a in range(32):
            countzero = 0
            for i in nums:
                if i&(1<<a):  countzero+=1
            ret += countzero*(n-countzero)
        return ret
            
        
        
        