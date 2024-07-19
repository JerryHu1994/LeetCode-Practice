class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.currnum = int("1"*len(characters), 2)
        self.combinationLength = combinationLength
        self.characters = characters

    def next(self) -> str:
        while self.currnum > 0:
            if bin(self.currnum).count('1') != self.combinationLength:
                self.currnum -= 1
            else:
                break
        ans = ""
        numstr = bin(self.currnum)[2:]
        if len(numstr) < len(self.characters):
            numstr = "0"*(len(self.characters) - len(numstr)) + numstr
        for ind, val in enumerate(numstr):
            if val == '1':
                ans += self.characters[ind]
        self.currnum -= 1
        return ans

    def hasNext(self) -> bool:
        while self.currnum > 0:
            if bin(self.currnum).count('1') == self.combinationLength:
                return True
            else:
                self.currnum -= 1
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()