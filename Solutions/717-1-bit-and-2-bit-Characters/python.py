class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        ind = 0
        while ind < len(bits):
            if bits[ind] == 0:
                ind += 1
            else:
                if ind == len(bits) - 2:    return False
                ind += 2
        return True