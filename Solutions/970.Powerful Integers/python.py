class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ans = set()
        if bound == 0:  return []
        x_upper, y_upper = int(math.ceil(math.log(bound)/math.log(x))) if x!=1 else 1, int(math.ceil(math.log(bound)/math.log(y))) if y!=1 else 1
        for i in range(x_upper):
            j = 0
            if y == 1:
                if x**i+y**j <= bound:  ans.add(x**i+y**j)
                continue
            while x**i+y**j <= bound:
                ans.add(x**i+y**j)
                j += 1
        for i in range(y_upper):
            j = 0
            if x == 1:
                if x**i+y**j <= bound:  ans.add(x**i+y**j)
                continue
            while x**j+y**i <= bound:
                ans.add(x**j+y**i)
                j += 1
        return list(ans)
        