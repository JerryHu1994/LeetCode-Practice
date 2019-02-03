class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g_sort,s_sort = sorted(g), sorted(s)
        ret = 0
        g_ind, s_ind = 0, 0
        while g_ind < len(g_sort) and s_ind < len(s_sort):
            if g_sort[g_ind] <= s_sort[s_ind]:
                g_ind += 1
                s_ind += 1
                ret += 1
            else:
                s_ind += 1
        return ret