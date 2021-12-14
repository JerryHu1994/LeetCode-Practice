class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        points = []
        for pos, lightrange in lights:
            points.append((pos-lightrange, "s"))
            points.append((pos+lightrange+1, "e"))
        points.sort()
        ans = points[0][0]
        ans_brightness = 1
        currbrightness = 0
        for pos, state in points:
            currbrightness += 1 if state == "s" else -1
            if currbrightness > ans_brightness:
                ans = pos
                ans_brightness = currbrightness
        return ans