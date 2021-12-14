class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        s = set()
        for c in word1:
            counter1[c] += 1
            s.add(c)
        for c in word2:
            counter2[c] += 1
            s.add(c)
        for char in s:
            if abs(counter1[char] - counter2[char]) > 3:
                return False
        return True