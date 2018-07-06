class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x, bin_y = bin(x)[2:], bin(y)[2:]
        l = min(len(bin_x), len(bin_y))
        cnt = 0
        for i in range(l):
            if bin_x[len(bin_x)-1-i] != bin_y[len(bin_y)-1-i]:
                cnt += 1
        left = bin_y if l == len(bin_x) else bin_x
        for i in range(len(left)-l):
            if left[i] == "1":
                cnt += 1
        return cnt