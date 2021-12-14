class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        count_k = 0
        for element in arr:
            if cnt[element] == 1:
                count_k += 1
            if count_k == k:    return element
        return ""