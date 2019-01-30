class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A>B:
            large, small, large_char, small_char = A, B, "a", "b"
        else:
            large, small, large_char, small_char = B, A, "b", "a"
        diff = min(large - small, small)
        ans = (large_char*2+small_char)*diff
        large, small = large-diff*2, small - diff
        if small == 0:
            ans += large_char*large
        else:
            ans += (large_char+small_char)*small
        return ans