# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> int:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        distmap = {}
        distmap[(0, 0)] = 0
        self.destination = None
        def dfs(currx, curry):
            if master.isTarget():
                self.destination = [currx, curry]
                return
            for direction, reversedir, nextx, nexty in ('U', 'D', currx, curry+1), ('D', 'U', currx, curry-1), ('L', 'R', currx-1, curry), ('R', 'L', currx+1, curry):
                if master.canMove(direction) and (nextx, nexty) not in distmap:
                    currcost = master.move(direction)
                    distmap[(nextx, nexty)] = currcost
                    dfs(nextx, nexty)
                    master.move(reversedir)

        dfs(0, 0)
        if self.destination == None: return -1
        heap = []
        heapq.heappush(heap, (0, 0, 0))
        while len(heap):
            cost, xcoord, ycoord = heapq.heappop(heap)
            #print (cost, xcoord, ycoord)
            if [xcoord, ycoord] == self.destination:
                return cost
            for nextx, nexty in (xcoord+1, ycoord), (xcoord-1, ycoord), (xcoord, ycoord+1), (xcoord, ycoord-1):
                if (nextx, nexty) in distmap:
                    heappush(heap, (cost + distmap[(nextx, nexty)], nextx, nexty))
                    distmap[(nextx, nexty)] = sys.maxsize
        return -1