class Solution(object):
    
    def helper(self, currstr, left, right):
        # exhausts
        if left == 0 and right == 0:
            self.sol.append(currstr)
            return
        # append left parenthesis
        if left > 0:
            self.helper(currstr + "(", left-1, right)
        if right > left:
            self.helper(currstr + ")", left, right-1)
        return 
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.sol = []
        self.helper("", n, n)
        return self.sol
        