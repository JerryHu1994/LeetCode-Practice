class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
            if freq[n] > 2: return False
        return True