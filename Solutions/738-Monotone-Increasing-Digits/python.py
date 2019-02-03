class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        li = [int(i) for i in str(N)]
        for i in range(len(li)-2, -1, -1):
            if li[i] <= li[i+1]:
                continue
            else:
                # set li[i] minus 1, and everything right to 9
                li[i] -= 1
                for j in range(i+1, len(li)):
                    li[j] = 9
        while li[0] == 0:
            li.pop(0)
        return int("".join([str(i) for i in li]))
            
                
            