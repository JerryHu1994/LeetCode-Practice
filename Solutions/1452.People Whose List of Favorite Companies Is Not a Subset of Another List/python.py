class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        peoplesets = [set(comp) for comp in favoriteCompanies]
        ans = set()
        for i, currset in enumerate(peoplesets):
            for j, compare in enumerate(peoplesets):
                if i == j:  continue
                if currset.issubset(compare):
                    ans.add(i)
                    break
        return [i for i in range(len(favoriteCompanies)) if i not in ans]