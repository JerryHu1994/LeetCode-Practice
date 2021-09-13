class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        sorted_props = sorted(properties, key=lambda x: (-x[0],x[1]))
        ans = 0
        curr_max = 0
        for attack, defence in sorted_props:
            if defence < curr_max:
                ans += 1
            else:
                curr_max = defence
        return ans