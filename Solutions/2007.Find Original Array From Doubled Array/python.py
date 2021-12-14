class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        sorted_changed = sorted(changed)
        if len(sorted_changed)%2 == 1:  return []
        counter = defaultdict(int)
        for i in changed:   counter[i] += 1
        ans = []
        for num in sorted_changed:
            if num not in counter:  continue
            if num*2 not in counter:
                return []
            else:
                ans.append(num)
                counter[num] -= 1
                if counter[num] == 0:   del counter[num]
                counter[num*2] -= 1
                if counter[num*2] == 0: del counter[num*2]
        return ans