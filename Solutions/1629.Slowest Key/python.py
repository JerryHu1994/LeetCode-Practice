class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        curr = 0
        maxValue = 0     
        
        for r in range(len(releaseTimes)):
            diff = releaseTimes[r] - curr
            if (diff > maxValue):
                maxValue = diff
                maxLetter = keysPressed[r]
            elif (diff == maxValue): # if max's are same check the value of the lettrs
                if keysPressed[r] > maxLetter:
                    maxLetter = keysPressed[r]
            curr = releaseTimes[r]
        
        return maxLetter