class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        cnt1, cnt2 = 0, 0
        for i in nums:
            if i == candidate1: cnt1 += 1
            if i == candidate2: cnt2 += 1
        ret = []
        if cnt1 > len(nums)/3:  ret.append(candidate1)
        if cnt2 > len(nums)/3:  ret.append(candidate2)
        return ret
            
            