class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        land_to_id = {} # maps (x,y) to island id
        id_to_land = collections.defaultdict(list) # maps island id to a list of (x,y)
        imap = [[0]*n for i in range(m)]
        nextid = 0
        ret = []
        for p in positions:
            neigh = []
            imap[p[0]][p[1]] = 1
            if p[0] > 0 and imap[p[0]-1][p[1]] == 1:    neigh.append((p[0]-1, p[1]))
            if p[0] < m-1 and imap[p[0]+1][p[1]] == 1:  neigh.append((p[0]+1, p[1]))
            if p[1] > 0 and imap[p[0]][p[1]-1] == 1:    neigh.append((p[0], p[1]-1))
            if p[1] < n-1 and imap[p[0]][p[1]+1] == 1:  neigh.append((p[0], p[1]+1))
            neighid = list(set([land_to_id[i] for i in neigh]))
            if len(neigh) == 0:
                # this is a new island
                land_to_id[(p[0], p[1])] = nextid
                id_to_land[nextid].append((p[0], p[1]))
                nextid += 1
            else:
                # let's merge to first neigh island id
                mergeid = neighid[0]
                # merge p
                land_to_id[(p[0], p[1])] = mergeid
                id_to_land[mergeid].append((p[0], p[1]))
                # merge the rest neighbors
                for ni in neighid[1:]:
                    currlands = id_to_land[ni]
                    for cl in currlands:
                        land_to_id[cl] = mergeid
                    id_to_land[mergeid] += currlands
                    del id_to_land[ni]
            ret.append(len(id_to_land))
        return ret
                

                                                
            