class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        height, width = len(nums), len(nums[0])
        if height*width != r*c: return nums
        idx = 0
        ret = []
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(nums[idx//width][idx%width])
                idx += 1
            ret.append(temp)
        return ret