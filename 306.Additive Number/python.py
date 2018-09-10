class Solution(object):
    def helper(self, prev1, prev2, num):
        if len(num) == 0:   return True
        len1 = max(len(prev1), len(prev2))
        len2 = len1 + 1
        presum = int(prev1) + int(prev2)
        if len(num) >= len1 and presum == int(num[:len1]):
            if len(num[:len1]) > 1 and num[:len1][0] == "0":    return False
            return self.helper(prev2, num[:len1], num[len1:])
        elif len(num) >= len2 and presum == int(num[:len2]):
            if len(num[:len2]) > 1 and num[:len2][0] == "0":    return False
            return self.helper(prev2, num[:len2], num[len2:])
        else:
            return False
    
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for first_end in range(1, len(num)/2+1):
            firstnum = num[:first_end]
            if len(firstnum) > 1 and firstnum[0] == "0":    continue
            for second_end in range(first_end+1, len(num)):
                secondnum = num[first_end:second_end]
                if len(secondnum) > 1 and secondnum[0] == "0":    continue
                if self.helper(firstnum, secondnum, num[second_end:]):  return True
        return False