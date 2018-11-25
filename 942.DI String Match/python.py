class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l = len(S)+1
        nums = [i for i in range(l)]
        ret = []
        for i in S:
            if i == "I":
                ret.append(nums.pop(0))
            else:
                ret.append(nums.pop(-1))
        ret.append(nums[0])
        return ret