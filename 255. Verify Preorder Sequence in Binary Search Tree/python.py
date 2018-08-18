class Solution(object):
    
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if len(preorder) == 0:   return True
        stack = [preorder[0]]
        ind = 1
        currbound = float("-inf")
        while ind < len(preorder):
            if preorder[ind] <= currbound:  return False
            if preorder[ind] < stack[-1]:
                stack.append(preorder[ind])
            else:
                while len(stack)>0 and stack[-1] < preorder[ind]:
                    currbound = stack.pop()
                stack.append(preorder[ind])
            ind += 1
        return True
                