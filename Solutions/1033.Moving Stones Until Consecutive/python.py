class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        min_ele, mid_ele, max_ele = sorted([a, b, c])
        if min_ele == mid_ele - 1 and mid_ele == max_ele - 1:    return [0, 0]
        min_move, max_move = 0, max_ele - min_ele - 2
        if min_ele == mid_ele - 2 or min_ele == mid_ele - 1 or mid_ele == max_ele - 2 or mid_ele == max_ele - 1:
            min_move = 1
        else:
            min_move = 2
        return [min_move, max_move]