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


# inputs are sorted
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = sorted(nums1), sorted(nums2)
        ptr1, ptr2 = 0, 0
        ret = []
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                ret.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
            else:
                ptr1 += 1
        return ret