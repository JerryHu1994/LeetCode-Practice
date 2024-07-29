class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        cnt = defaultdict(int)
        for ind, sender in enumerate(senders):
            cnt[sender] += len(messages[ind].split())
        ans, largest = "", 0
        print (cnt)
        for k,v in cnt.items():
            if v > largest:
                ans, largest = k, v
            elif v == largest and k > ans:
                ans, largest = k, v
        return ans