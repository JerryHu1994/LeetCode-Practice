class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        total_len = len(arr)
        kv_pair = [(v, k) for k, v in cnt.items()]
        kv_pair = sorted(kv_pair, reverse = True)
        curr_cnt = 0
        set_count = 0
        for count, keyvalue in kv_pair:
            curr_cnt += count
            set_count += 1
            if curr_cnt >= total_len//2:
                return set_count
        