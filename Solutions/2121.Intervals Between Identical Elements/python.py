class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        l = len(arr)
        ans = [0]*l
        foward_scan_sum = defaultdict(int)
        foward_scan_cnt = defaultdict(int)
        for ind, val in enumerate(arr):
            ans[ind] += ind*foward_scan_cnt[val] - foward_scan_sum[val]
            foward_scan_sum[val] += ind
            foward_scan_cnt[val] += 1
        backward_scan_sum = defaultdict(int)
        backward_scan_cnt = defaultdict(int)
        for ind, val in enumerate(arr[::-1]):
            ans[l-1-ind] += ind*backward_scan_cnt[val] - backward_scan_sum[val]
            backward_scan_sum[val] += ind
            backward_scan_cnt[val] += 1
        return ans