class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_set = set(["".join(sorted(w)) for w in startWords])
        count = 0
        for targetword in targetWords:
            if len(targetword) > 1:
                sorted_targetword = "".join(sorted(targetword))
                for ind in range(len(sorted_targetword)):
                    if sorted_targetword[:ind]+sorted_targetword[ind+1:] in start_set:
                        count += 1
                        break
        return count