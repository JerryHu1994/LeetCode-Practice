class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        plants_with_pos = [(ind, val) for ind,val in enumerate(plants)]
        curr_pos = -1
        curr_cap = capacity
        ans = 0
        while len(plants_with_pos) > 0:
            next_pos, next_water = plants_with_pos.pop(0)
            if next_water > curr_cap:
                ans += curr_pos + next_pos + 2
                curr_pos = next_pos
                curr_cap = capacity - next_water
            else:
                ans += next_pos - curr_pos
                curr_pos = next_pos
                curr_cap -= next_water
        return ans