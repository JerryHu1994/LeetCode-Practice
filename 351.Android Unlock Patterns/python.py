class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ret = 0
        jumps = {(1,3) : 2, (3,1) : 2, (1, 7) : 4, (7,1) : 4, (3, 9):6, (9,3): 6, (7,9) : 8, (9,7) : 8, (2, 8) : 5, (8,2) :5, (4,6):5, (6,4) : 5, (1,9):5, (9,1):5, (3,7):5, (7,3):5}
        def helper(curr_list, res):
            if m <= len(curr_list) <= n:
                res += 1
            if len(curr_list) > n:
                return res
            for i in range(1, 10):
                if i in curr_list:    continue
                # check if i is allowed
                if (curr_list[-1], i) in jumps and jumps[(curr_list[-1], i)] not in curr_list:
                    continue
                res = helper(curr_list+[i], res)
            return res
        ret += helper([1], 0)*4
        ret += helper([2], 0)*4
        ret += helper([5], 0)
        return ret