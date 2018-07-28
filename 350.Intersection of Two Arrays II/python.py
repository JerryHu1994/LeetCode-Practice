class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        cnt1 = collections.Counter(nums1)
        cnt2 = collections.Counter()
        for i in nums2:
            if i not in cnt1:
                continue
            elif cnt2[i] < cnt1[i]:
                cnt2[i] += 1
        ret = []
        for key, val in cnt2.items():
            ret += [key]*val
        return ret