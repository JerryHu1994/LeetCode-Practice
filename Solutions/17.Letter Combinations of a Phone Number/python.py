class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:  return []
        li = [[], [], ["a", "b", "c"], ["d", "e", "f"], ["g","h","i"], ["j","k","l"], ["m","n","o"], ["p","q","r","s"], ["t","u","v"], ["w","x","y","z"]]
        return self.helper(li, digits)
        
    def helper(self,li, digits):
        if len(digits) == 1:    return li[int(digits)]
        ret = []
        num = int(digits[0])
        for j in li[num]:
            curlist = self.helper(li, digits[1:])
            for k in curlist:
                ret.append(j+k)
        return ret
            
        
        