class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        n, viewsum_dic, bestview = len(creators), defaultdict(int), {}
        bestviewcount = 0
        for creator, videoid, view in zip(creators, ids, views):
            viewsum_dic[creator] += view
            bestviewcount = max(bestviewcount, viewsum_dic[creator])
            if creator in bestview:
                curr_bestvideo, curr_bestview = bestview[creator]
                if view > curr_bestview:
                    bestview[creator] = (videoid, view)
                elif view == curr_bestview:
                    if videoid < curr_bestvideo:
                        bestview[creator] = (videoid, view)
            else:
                bestview[creator] = (videoid, view)
        best_creator = [bestcreator for bestcreator, viewsum in viewsum_dic.items() if viewsum == bestviewcount]
        return [[creator, bestview[creator][0]] for creator in best_creator]