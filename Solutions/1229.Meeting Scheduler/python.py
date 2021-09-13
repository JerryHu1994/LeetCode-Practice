class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1, slots2 = sorted(slots1), sorted(slots2)
        ptr1, ptr2 = 0, 0
        while ptr1 < len(slots1) and ptr2 < len(slots2):
            start1, end1 = slots1[ptr1]
            start2, end2 = slots2[ptr2]
            if end1 <= start2:
                ptr1 += 1
            elif end2 <= start1:
                ptr2 += 1
            else:
                overlapstart, overlapend = max(start1, start2), min(end1, end2)
                if overlapend - overlapstart >= duration:
                    return [overlapstart, overlapstart+duration]
                if end1 < end2:
                    ptr1 += 1
                else:
                    ptr2 += 1
        return []