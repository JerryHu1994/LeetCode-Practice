class Solution:
    def minDeletions(self, s: str) -> int:
        cnter = Counter(s)
        fre_set = set()
        dup_list = []
        for char in cnter:
            if cnter[char] not in fre_set:
                fre_set.add(cnter[char])
            else:
                dup_list.append(cnter[char])
        ans = 0
        for dup in dup_list:
            curr = dup
            while curr in fre_set and curr != 0:
                curr -= 1
            ans += dup - curr
            if curr != 0:   fre_set.add(curr)
        return ans
            