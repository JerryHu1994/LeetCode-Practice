class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        maxarea = min(height[left], height[right])*(len(height)-1)
        while left < right:
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
            maxarea = max(maxarea, (right-left)*min(height[left], height[right]))
        return maxarea
            
                