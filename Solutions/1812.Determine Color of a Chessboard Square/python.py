class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = coordinates[0], coordinates[1]
        oddcoods = set(["a", "c", "e", "g"])
        y = int(y)
        if (x in oddcoods and y%2==1) or (x not in oddcoods and y%2==0):
            return False
        else:
            return True