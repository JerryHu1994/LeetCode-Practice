class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if len(rooms)==0:   return
        height, width = len(rooms), len(rooms[0])
        for i in range(height):
            for j in range(width):
                # check if curr is a gate
                if rooms[i][j] == 0:
                    queue = [(i, j, 0)]
                    s = set()
                    while len(queue):
                        curry, currx, dis = queue.pop(0)
                        s.add((curry, currx))
                        if dis != 0:
                            rooms[curry][currx] = min(rooms[curry][currx], dis)
                        # left 
                        if currx > 0 and rooms[curry][currx-1] != 0 and rooms[curry][currx-1] != -1 and (curry, currx-1) not in s:
                            queue.append((curry, currx-1, dis+1))
                        # down
                        if curry < height-1 and rooms[curry+1][currx] != 0 and rooms[curry+1][currx] != -1 and (curry+1, currx) not in s:
                            queue.append((curry+1, currx, dis+1))
                        # right
                        if currx < width-1 and rooms[curry][currx+1] != 0 and rooms[curry][currx+1] != -1 and (curry, currx+1) not in s:
                            queue.append((curry, currx+1, dis+1))
                        # up
                        if curry > 0 and rooms[curry-1][currx] != 0 and rooms[curry-1][currx] != -1 and (curry-1, currx) not in s:
                            queue.append((curry-1, currx, dis+1))
                        