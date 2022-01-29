class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans, l = [], len(s)
        dic = { "R":(0, 1), "D":(1, 0), "L":(0, -1), "U":(-1, 0)}
        for ind in range(l):
            cnt = 0
            curry, currx = startPos
            endlist = True
            for i in range(ind, l):
                diry, dirx = dic[s[i]]
                curry += diry
                currx += dirx
                if curry < 0 or curry >= n or currx < 0 or currx >= n:
                    endlist = False
                    ans.append(cnt)
                    break
                else:
                    cnt += 1
            if endlist:
                ans.append(l-ind)
        return ans