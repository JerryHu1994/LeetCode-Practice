class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        ind = 0
        if m*n != len(original): return []
        while ind < len(original):
            ans.append(original[ind:ind+n])
            ind += n
        return ans