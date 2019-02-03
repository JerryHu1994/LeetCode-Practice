class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        low, high = ord('a'), ord('z')
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]
        ret = ""
        for ind, c in enumerate(S):
            ret += chr(low + (ord(c) + shifts[ind] - low)%26)
        return ret
            