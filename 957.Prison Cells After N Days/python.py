class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        l = len(cells)
        mem = {}
        reverse = {}
        for i in range(min(2**8, N)):
            nextcells = [0]*l
            for j in range(1, l-1):
                if cells[j-1] == cells[j+1]:
                    nextcells[j] = 1
            cells = nextcells
            if tuple(cells) in mem:
                prev = mem[tuple(cells)]
                cycle = i+1-prev
                ind = (N)%cycle
                if ind == 0:    return list(reverse[prev+cycle-1])
                return list(reverse[ind])
            mem[tuple(cells)] = i+1
            reverse[i+1] = tuple(cells)
        return cells