class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        limit = len(arr)/4
        cnt = defaultdict(int)
        for n in arr:
            cnt[n] += 1
            if cnt[n] > limit:  return n
        
        