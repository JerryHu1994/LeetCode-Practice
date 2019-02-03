class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        currdiridx, currpos, ret = 0, [0,0], 0
        obs = set([(i[0], i[1]) for i in obstacles])
        for com in commands:
            if com == -2:
                currdiridx = (currdiridx - 1 + 4)%4
            elif com == -1:
                currdiridx = (currdiridx + 1)%4
            else:
                currdir = dirs[currdiridx]
                for i in range(com):
                    nextpos = (currpos[0]+currdir[0], currpos[1]+currdir[1])
                    if nextpos in obs:
                        break
                    else:
                        currpos = list(nextpos)
                    ret = max(ret, currpos[0]**2 + currpos[1]**2)
        return ret