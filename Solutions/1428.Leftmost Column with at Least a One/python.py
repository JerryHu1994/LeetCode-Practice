# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        height, width = binaryMatrix.dimensions()
        curry, currx = 0, width-1
        foundone = False
        while currx >= 0 and curry < height:
            if binaryMatrix.get(curry, currx) == 1:
                foundone = True
                if currx - 1 >= 0 and binaryMatrix.get(curry, currx-1) == 1:
                    currx -= 1
                else:
                    curry += 1
            else:
                curry += 1
        return currx if foundone else -1