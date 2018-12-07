class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        mem = {}
        startstate = "0"*(maxChoosableInteger+1)
        if sum([i for i in range(1, maxChoosableInteger+1)]) < desiredTotal:    return False
        if desiredTotal == 0: return True
        def helper(currstate, target):
            if (currstate, target) in mem:  return mem[(currstate, target)]
            for i in range(maxChoosableInteger, 0, -1):
                if currstate[i] == "0":
                    if i >= target:  return True
                    ret = helper(currstate[:i]+"1"+currstate[i+1:], target-i)
                    if not ret:
                        mem[(currstate, target)] = True
                        return True
            mem[(currstate, target)] = False
            return False
        return helper(startstate, desiredTotal)