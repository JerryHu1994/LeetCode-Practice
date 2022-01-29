class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_q, negative_q = [n for n in nums if n > 0], [n for n in nums if n < 0]
        ans = []
        for i in range(len(positive_q)):
            ans.append(positive_q[i])
            ans.append(negative_q[i])
        return ans