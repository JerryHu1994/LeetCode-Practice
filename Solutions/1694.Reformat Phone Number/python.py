class Solution:
    def reformatNumber(self, number: str) -> str:
        curr = ""
        ans = []
        for val in number:
            if val == " " or val == "-":    continue
            curr += val
            if len(curr) == 3:
                ans.append(curr)
                curr = ""
        if len(curr) == 1:
            last = ans.pop()
            ans.append(last[0:2])
            ans.append(last[-1] + curr)
        elif len(curr) == 2:
            ans.append(curr)
        return "-".join(ans)