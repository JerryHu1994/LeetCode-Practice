
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        dp_sum = [[0]*l for i in range(l)]
        for i in range(l):
            for j in range(i, l):
                if j == i:
                    dp_sum[i][j] = nums[i]
                else:
                    dp_sum[i][j] = dp_sum[i][j-1] + nums[j]
        for mid in range(3, l-3):
            currset = set()
            for i in range(1, mid-1):
                if dp_sum[0][i-1] == dp_sum[i+1][mid-1]:
                    # first two match
                    currset.add(dp_sum[0][i-1])
            for j in range(mid+2, l-1):
                if dp_sum[mid+1][j-1] == dp_sum[j+1][l-1] and dp_sum[j+1][l-1] in currset:
                    return True
        return False
                
                
         
        