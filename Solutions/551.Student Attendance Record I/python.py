class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_a, count_l = 0, 0
        for i in s:
            if i == 'A':
                count_a += 1
            if i == 'L':
                count_l += 1
            else:
                count_l = 0
            if count_l > 2: return False
        return False if count_a > 1 or count_l > 2 else True
        