class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        li = [0, 1]
        if n == 0:  return 0
        if n == 1:  return 1
        for i in range(2, n+1):
            if i%2 == 0:
                li.append(li[int(i/2)])
            else:
                div = int((i-1)/2)
                li.append(li[div] + li[div+1])
        return max(li)