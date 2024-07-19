class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:    return num
        if num > 0:
            zerocount = 0
            intlist = []
            for i in str(num):
                if int(i) == 0:
                    zerocount += 1
                else:
                    intlist.append(int(i))
            intlist.sort()
            ans = str(intlist[0])
            ans += "0"*zerocount
            ans += "".join([str(i)  for i in intlist[1:]])
            return int(ans)
        else:
            num = -num
            intlist = sorted([int(i)   for i in str(num)], reverse=True)
            strings = [str(i)   for i in intlist]
            return (-1)*int("".join(strings))