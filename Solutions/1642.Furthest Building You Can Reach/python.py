class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        curr_bricks = 0
        heap = []
        curr_small = None
        for i in range(0, len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if ladders == 0:
                    bricks -= diff
                    if bricks < 0:  return i
                else:
                    if len(heap) < ladders:
                        heapq.heappush(heap, diff)
                        curr_small = diff if curr_small == None else min(curr_small, diff)
                    elif curr_small == None or curr_small < diff:
                        use_brick = heapq.heappop(heap)
                        bricks -= use_brick
                        if bricks < 0:  return i
                        heapq.heappush(heap, diff)
                        curr_small = heapq.nsmallest(1, heap)[0]
                    else:
                        bricks -= diff
                        if bricks < 0:  return i
        return len(heights)-1