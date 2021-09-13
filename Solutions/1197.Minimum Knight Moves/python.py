class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        visited = set()
        visited.add((0,0))
        queue = [(0, 0)]
        curr_dis = 0
        nextq = []
        while len(queue):
            for (currx, curry) in queue:
                if currx == x and curry == y:   return curr_dis
                next_moves = [(currx+1, curry+2), (currx+2, curry+1), (currx+1, curry-2), (currx+2, curry-1),
                             (currx-1, curry+2), (currx-1, curry-2), (currx-2, curry+1), (currx-2, curry-1)]
                for (nextx, nexty) in next_moves:
                    if (nextx, nexty) not in visited:
                        visited.add((nextx, nexty))
                        nextq.append((nextx, nexty))
            queue = nextq
            nextq = []
            curr_dis += 1