class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters)-1
        while left < right:
            mid = (left + right)/2
            if ord(letters[mid]) <= ord(target):
                left = mid+1
            else:
                right = mid
        if left == len(letters)-1 and ord(letters[left]) <= ord(target):
            return letters[0]
        return letters[left]
        
            