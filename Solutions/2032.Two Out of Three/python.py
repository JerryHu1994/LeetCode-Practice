class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        num1_set = list(set(nums1))
        num2_set = list(set(nums2))
        num3_set = list(set(nums3))
        combined = num1_set + num2_set + num3_set
        dic = defaultdict(int)
        ans = []
        for element in combined:
            dic[element] += 1
            if dic[element] == 2:
                ans.append(element)
        return ans